import os
from pathlib import Path
from typing import List
from langchain.document_loaders import (
    PyPDFLoader,
    TextLoader,
    DirectoryLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

class BloomWatchDocumentProcessor:
    """
    Processes agricultural documents and creates a searchable knowledge base
    for the BloomWatch chatbot
    """
    
    def __init__(self, 
                 knowledge_base_path: str = "./knowledge_base",
                 vector_db_path: str = "./vector_db",
                 embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize the document processor
        
        Args:
            knowledge_base_path: Path to folder containing source documents
            vector_db_path: Path where vector database will be stored
            embedding_model: HuggingFace model for embeddings
        """
        self.knowledge_base_path = Path(knowledge_base_path)
        self.vector_db_path = Path(vector_db_path)
        
        print(f"🌾 Initializing BloomWatch Document Processor...")
        print(f"📁 Knowledge Base: {self.knowledge_base_path}")
        print(f"💾 Vector DB: {self.vector_db_path}")
        
        # Initialize embedding model
        print(f"🤖 Loading embedding model: {embedding_model}")
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs={'device': 'cpu'},  # Change to 'cuda' if GPU available
            encode_kwargs={'normalize_embeddings': True}
        )
        
        self.vector_store = None
        
    def load_documents(self) -> List:
        """
        Load all documents from the knowledge base folder
        Supports: PDF, TXT files
        """
        documents = []
        
        print("\n📚 Loading documents...")
        
        # Load PDFs
        pdf_loader = DirectoryLoader(
            str(self.knowledge_base_path),
            glob="**/*.pdf",
            loader_cls=PyPDFLoader,
            show_progress=True
        )
        pdf_docs = pdf_loader.load()
        documents.extend(pdf_docs)
        print(f"✅ Loaded {len(pdf_docs)} PDF documents")
        
        # Load text files
        txt_loader = DirectoryLoader(
            str(self.knowledge_base_path),
            glob="**/*.txt",
            loader_cls=TextLoader,
            show_progress=True
        )
        txt_docs = txt_loader.load()
        documents.extend(txt_docs)
        print(f"✅ Loaded {len(txt_docs)} text documents")
        
        print(f"\n📊 Total documents loaded: {len(documents)}")
        return documents
    
    def split_documents(self, documents: List, 
                       chunk_size: int = 1000,
                       chunk_overlap: int = 200) -> List:
        """
        Split documents into smaller chunks for better retrieval
        
        Args:
            documents: List of loaded documents
            chunk_size: Size of each chunk in characters
            chunk_overlap: Overlap between chunks to maintain context
        """
        print(f"\n✂️  Splitting documents into chunks...")
        print(f"   Chunk size: {chunk_size} characters")
        print(f"   Overlap: {chunk_overlap} characters")
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        
        chunks = text_splitter.split_documents(documents)
        print(f"✅ Created {len(chunks)} chunks")
        
        return chunks
    
    def create_vector_store(self, chunks: List):
        """
        Create and persist the vector database
        
        Args:
            chunks: Document chunks to embed and store
        """
        print(f"\n🔮 Creating vector database...")
        print(f"   This may take a few minutes...")
        
        # Create vector store
        self.vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=str(self.vector_db_path),
            collection_name="bloomwatch_agriculture"
        )
        
        # Persist to disk
        self.vector_store.persist()
        print(f"✅ Vector database created and saved to {self.vector_db_path}")
        
    def process_all(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Complete pipeline: Load -> Split -> Embed -> Store
        """
        print("="*60)
        print("🌾 BLOOMWATCH KNOWLEDGE BASE CREATION")
        print("="*60)
        
        # Step 1: Load documents
        documents = self.load_documents()
        
        if len(documents) == 0:
            print("⚠️  No documents found! Please add documents to the knowledge_base folder.")
            return
        
        # Step 2: Split into chunks
        chunks = self.split_documents(documents, chunk_size, chunk_overlap)
        
        # Step 3: Create vector store
        self.create_vector_store(chunks)
        
        print("\n" + "="*60)
        print("✅ KNOWLEDGE BASE READY!")
        print("="*60)
        
    def load_existing_vector_store(self):
        """
        Load an existing vector database
        """
        print(f"📂 Loading existing vector database from {self.vector_db_path}")
        
        self.vector_store = Chroma(
            persist_directory=str(self.vector_db_path),
            embedding_function=self.embeddings,
            collection_name="bloomwatch_agriculture"
        )
        
        print("✅ Vector database loaded successfully")
        return self.vector_store


# Usage Example
if __name__ == "__main__":
    # Initialize processor
    processor = BloomWatchDocumentProcessor(
        knowledge_base_path="./knowledge_base",
        vector_db_path="./vector_db"
    )
    
    # Process all documents (run this once when you add new documents)
    processor.process_all(chunk_size=1000, chunk_overlap=200)
    
    # To load existing database later:
    # vector_store = processor.load