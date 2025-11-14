#!/usr/bin/env python3
"""
quick_setup.py
One-command setup for BloomWatch chatbot testing
Runs all necessary steps automatically
"""

import subprocess
import sys
import os
from pathlib import Path

def print_header(text):
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")

def run_command(cmd, description):
    """Run a command and show progress"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✅ {description} - Done!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed!")
        print(f"Error: {e.stderr}")
        return False

def check_file_exists(filepath):
    """Check if a file exists"""
    return Path(filepath).exists()

def main():
    print_header("🌾 BLOOMWATCH CHATBOT - QUICK SETUP")
    
    print("This script will:")
    print("  1. Create mock knowledge base")
    print("  2. Process documents into vector database")
    print("  3. Start the FastAPI server")
    print("  4. Run basic tests")
    print("\nEstimated time: 5-10 minutes\n")
    
    input("Press Enter to continue or Ctrl+C to cancel...")
    
    # Step 1: Check if files exist
    print_header("📋 Step 1: Checking Required Files")
    
    required_files = [
        'create_mock_knowledge_base.py',
        'document_processor.py',
        'rag_chatbot.py',
        'main.py'
    ]
    
    missing_files = [f for f in required_files if not check_file_exists(f)]
    
    if missing_files:
        print("❌ Missing required files:")
        for f in missing_files:
            print(f"   - {f}")
        print("\nPlease ensure all code files are in the current directory.")
        sys.exit(1)
    
    print("✅ All required files found!")
    
    # Step 2: Create knowledge base
    print_header("📚 Step 2: Creating Mock Knowledge Base")
    
    if not run_command(
        f"{sys.executable} create_mock_knowledge_base.py",
        "Creating knowledge base"
    ):
        print("\n⚠️  Failed to create knowledge base. Exiting...")
        sys.exit(1)
    
    # Check if knowledge base was created
    kb_path = Path("knowledge_base")
    if not kb_path.exists():
        print("❌ Knowledge base directory not created!")
        sys.exit(1)
    
    # Count files
    txt_files = list(kb_path.rglob("*.txt"))
    print(f"\n📊 Created {len(txt_files)} knowledge base documents")
    
    # Step 3: Process documents
    print_header("🔮 Step 3: Processing Documents & Creating Vector Database")
    print("⏳ This may take 2-5 minutes depending on your system...\n")
    
    if not run_command(
        f"{sys.executable} document_processor.py",
        "Processing documents"
    ):
        print("\n⚠️  Failed to process documents. Exiting...")
        sys.exit(1)
    
    # Check if vector DB was created
    vdb_path = Path("vector_db")
    if not vdb_path.exists():
        print("❌ Vector database not created!")
        sys.exit(1)
    
    print("\n✅ Vector database created successfully!")
    
    # Step 4: Test the setup
    print_header("🧪 Step 4: Running Quick Test")
    
    # Create a simple test script
    test_script = """
import sys
try:
    from rag_chatbot import BloomWatchChatbot
    print("✅ Chatbot module loads successfully")
    
    # Try to initialize (this validates vector DB)
    chatbot = BloomWatchChatbot(vector_db_path="./vector_db", device="cpu")
    print("✅ Chatbot initializes successfully")
    
    # Try a simple query
    response = chatbot.chat("What is NDVI?", language="en")
    if response and 'answer' in response:
        print("✅ Chatbot responds to queries")
        print(f"\\nSample response: {response['answer'][:150]}...")
    else:
        print("❌ Chatbot response format incorrect")
        sys.exit(1)
        
    print("\\n✅ All systems operational!")
    sys.exit(0)
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
"""
    
    # Write test script
    with open("_quick_test.py", "w") as f:
        f.write(test_script)
    
    print("🔄 Testing chatbot initialization...")
    if not run_command(f"{sys.executable} _quick_test.py", "System test"):
        print("\n⚠️  System test failed. Please check the errors above.")
        sys.exit(1)
    
    # Clean up test script
    os.remove("_quick_test.py")
    
    # Step 5: Instructions for starting server
    print_header("🎉 SETUP COMPLETE!")
    
    print("✅ Knowledge base created (8 documents)")
    print("✅ Vector database ready")
    print("✅ System tested and operational\n")
    
    print("📋 NEXT STEPS:")
    print("\n1. Start the server:")
    print("   python main.py")
    print("\n2. In a new terminal, run tests:")
    print("   python test_api.py")
    print("\n3. Or test manually:")
    print("   Open http://localhost:8000/docs in your browser")
    print("\n4. Example API call:")
    print('''   curl -X POST "http://localhost:8000/chat" \\
     -H "Content-Type: application/json" \\
     -d '{
       "query": "What does NDVI tell me about crop health?",
       "language": "en"
     }'
''')
    
    print("\n" + "="*70)
    print("🌾 BloomWatch is ready to help farmers!")
    print("="*70 + "\n")
    
    # Ask if user wants to start server now
    start_server = input("Would you like to start the server now? (y/n): ")
    
    if start_server.lower() in ['y', 'yes']:
        print("\n🚀 Starting BloomWatch server...")
        print("Press Ctrl+C to stop the server\n")
        try:
            subprocess.run(f"{sys.executable} main.py", shell=True)
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped. Thank you for using BloomWatch!")
    else:
        print("\n👋 Setup complete! Run 'python main.py' when you're ready.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)