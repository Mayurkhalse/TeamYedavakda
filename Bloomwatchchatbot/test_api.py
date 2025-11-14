# test_api.py
# Comprehensive testing script for BloomWatch chatbot API

import requests
import json
import time
from typing import Dict, List

class BloomWatchAPITester:
    """Test suite for BloomWatch chatbot API"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.test_results = []
        
    def print_section(self, title: str):
        """Print formatted section header"""
        print("\n" + "="*60)
        print(f"  {title}")
        print("="*60)
    
    def test_health_check(self) -> bool:
        """Test if the API is running"""
        self.print_section("🏥 Testing Health Check")
        
        try:
            response = requests.get(f"{self.base_url}/health")
            result = response.json()
            
            print(f"Status Code: {response.status_code}")
            print(f"Server Status: {result['status']}")
            print(f"Chatbot Loaded: {result['chatbot_loaded']}")
            
            if response.status_code == 200 and result['chatbot_loaded']:
                print("✅ Health check passed!")
                return True
            else:
                print("❌ Health check failed!")
                return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def test_basic_query(self) -> bool:
        """Test basic chat query without farm data"""
        self.print_section("💬 Testing Basic Query")
        
        payload = {
            "query": "What is NDVI and why is it important for farmers?",
            "language": "en"
        }
        
        try:
            print(f"Query: {payload['query']}")
            
            start_time = time.time()
            response = requests.post(f"{self.base_url}/chat", json=payload)
            end_time = time.time()
            
            result = response.json()
            
            print(f"\nResponse Time: {end_time - start_time:.2f} seconds")
            print(f"\nAnswer: {result['answer'][:300]}...")
            print(f"\nSources Used: {len(result['sources'])} documents")
            print(f"Language: {result['language']}")
            
            if response.status_code == 200:
                print("✅ Basic query test passed!")
                return True
            else:
                print("❌ Basic query test failed!")
                return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def test_query_with_farm_data(self) -> bool:
        """Test query with complete farm data"""
        self.print_section("🌾 Testing Query with Farm Data")
        
        farm_data = {
            "location": "Pune, Maharashtra",
            "ndvi": 0.72,
            "evi": 0.65,
            "crop_type": "Wheat",
            "soil_type": "Black soil (Regur)",
            "area": 5.5,
            "suggested_crops": ["Cotton", "Soybean", "Sorghum"],
            "rainfall": 25.5,
            "temperature": 28.3
        }
        
        payload = {
            "query": "Based on my current NDVI value, how healthy is my wheat crop?",
            "language": "en",
            "farm_data": farm_data,
            "user_id": "test_farmer_001"
        }
        
        try:
            print(f"Query: {payload['query']}")
            print(f"\nFarm Context:")
            for key, value in farm_data.items():
                print(f"  {key}: {value}")
            
            start_time = time.time()
            response = requests.post(f"{self.base_url}/chat", json=payload)
            end_time = time.time()
            
            result = response.json()
            
            print(f"\nResponse Time: {end_time - start_time:.2f} seconds")
            print(f"\nAnswer: {result['answer'][:300]}...")
            print(f"\nFarm Data Used: {result['farm_data_used']}")
            print(f"Sources: {', '.join(result['sources'][:2])}")
            
            if response.status_code == 200 and result['farm_data_used']:
                print("✅ Farm data query test passed!")
                return True
            else:
                print("❌ Farm data query test failed!")
                return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def test_multilingual_hindi(self) -> bool:
        """Test Hindi language support"""
        self.print_section("🌐 Testing Hindi Translation")
        
        payload = {
            "query": "मेरी मिट्टी के लिए कौन सी फसल सबसे अच्छी है?",
            "language": "hi",
            "farm_data": {
                "location": "पुणे",
                "soil_type": "काली मिट्टी"
            }
        }
        
        try:
            print(f"Query (Hindi): {payload['query']}")
            print("Translation: Which crop is best for my soil?")
            
            start_time = time.time()
            response = requests.post(f"{self.base_url}/chat", json=payload)
            end_time = time.time()
            
            result = response.json()
            
            print(f"\nResponse Time: {end_time - start_time:.2f} seconds")
            print(f"\nAnswer (Hindi): {result['answer'][:200]}...")
            print(f"Language Detected: {result['language']}")
            
            if response.status_code == 200:
                print("✅ Hindi translation test passed!")
                return True
            else:
                print("❌ Hindi translation test failed!")
                return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def test_batch_queries(self) -> bool:
        """Test batch query endpoint"""
        self.print_section("📦 Testing Batch Queries")
        
        queries = [
            {
                "query": "How much nitrogen fertilizer for wheat?",
                "language": "en"
            },
            {
                "query": "What are signs of pest infestation?",
                "language": "en"
            },
            {
                "query": "Best irrigation schedule for cotton?",
                "language": "en"
            }
        ]
        
        try:
            print(f"Processing {len(queries)} queries...")
            
            start_time = time.time()
            response = requests.post(f"{self.base_url}/chat/batch", json=queries)
            end_time = time.time()
            
            result = response.json()
            
            print(f"\nResponse Time: {end_time - start_time:.2f} seconds")
            print(f"Total Responses: {result['total']}")
            
            for i, resp in enumerate(result['responses'][:2], 1):
                print(f"\nResponse {i}: {resp['answer'][:150]}...")
            
            if response.status_code == 200:
                print("✅ Batch query test passed!")
                return True
            else:
                print("❌ Batch query test failed!")
                return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def test_system_info(self) -> bool:
        """Test system info endpoint"""
        self.print_section("ℹ️  Testing System Info")
        
        try:
            response = requests.get(f"{self.base_url}/info")
            result = response.json()
            
            print(f"Name: {result['name']}")
            print(f"Version: {result['version']}")
            print(f"Status: {result['status']}")
            print(f"\nCapabilities:")
            for cap in result['capabilities']:
                print(f"  • {cap}")
            print(f"\nSupported Languages: {', '.join(result['supported_languages'])}")
            
            if response.status_code == 200:
                print("✅ System info test passed!")
                return True
            else:
                print("❌ System info test failed!")
                return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def test_agriculture_specific_queries(self) -> bool:
        """Test agriculture-specific queries"""
        self.print_section("🌱 Testing Agriculture-Specific Queries")
        
        test_cases = [
            {
                "name": "NDVI Interpretation",
                "query": "My NDVI is 0.45. What does this mean?",
                "farm_data": {"ndvi": 0.45, "crop_type": "Rice"}
            },
            {
                "name": "Fertilizer Recommendation",
                "query": "What NPK ratio should I use for cotton in black soil?",
                "farm_data": {"crop_type": "Cotton", "soil_type": "Black soil"}
            },
            {
                "name": "Pest Management",
                "query": "How do I identify and control whitefly in cotton?",
                "farm_data": {"crop_type": "Cotton"}
            }
        ]
        
        passed = 0
        
        for test in test_cases:
            print(f"\n📝 Test: {test['name']}")
            print(f"Query: {test['query']}")
            
            payload = {
                "query": test['query'],
                "language": "en",
                "farm_data": test.get('farm_data')
            }
            
            try:
                response = requests.post(f"{self.base_url}/chat", json=payload)
                result = response.json()
                
                if response.status_code == 200:
                    print(f"✅ Answer received: {result['answer'][:150]}...")
                    passed += 1
                else:
                    print(f"❌ Failed with status {response.status_code}")
                    
            except Exception as e:
                print(f"❌ Error: {e}")
        
        print(f"\n{'='*60}")
        print(f"Passed: {passed}/{len(test_cases)} tests")
        
        return passed == len(test_cases)
    
    def run_all_tests(self):
        """Run complete test suite"""
        print("\n" + "="*60)
        print("  🌾 BLOOMWATCH API TEST SUITE")
        print("="*60)
        
        tests = [
            ("Health Check", self.test_health_check),
            ("Basic Query", self.test_basic_query),
            ("Farm Data Query", self.test_query_with_farm_data),
            ("Hindi Translation", self.test_multilingual_hindi),
            ("Batch Queries", self.test_batch_queries),
            ("System Info", self.test_system_info),
            ("Agriculture Queries", self.test_agriculture_specific_queries)
        ]
        
        results = []
        
        for test_name, test_func in tests:
            try:
                result = test_func()
                results.append((test_name, result))
            except Exception as e:
                print(f"❌ {test_name} crashed: {e}")
                results.append((test_name, False))
            
            time.sleep(1)  # Small delay between tests
        
        # Summary
        self.print_section("📊 TEST SUMMARY")
        
        passed = sum(1 for _, result in results if result)
        total = len(results)
        
        for test_name, result in results:
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{status} - {test_name}")
        
        print(f"\n{'='*60}")
        print(f"Total: {passed}/{total} tests passed ({(passed/total)*100:.1f}%)")
        print(f"{'='*60}\n")
        
        return passed == total


# Main execution
if __name__ == "__main__":
    import sys
    
    # Check if API URL provided
    api_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    
    print(f"Testing API at: {api_url}")
    
    # Create tester instance
    tester = BloomWatchAPITester(base_url=api_url)
    
    # Run all tests
    all_passed = tester.run_all_tests()
    
    # Exit with appropriate code
    sys.exit(0 if all_passed else 1)