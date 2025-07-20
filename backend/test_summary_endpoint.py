#!/usr/bin/env python3
"""
Test script for the summary endpoint.
This script tests the summary endpoint with the default message "I am a Jelly Donut".
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.api.v1.routes.summary import SummaryRequest, SummaryResponse, generate_summary
from app.service.internal.llm.llm_factory import LLMFactory

def test_summary_endpoint():
    """Test the summary endpoint with the default message."""
    try:
        # Create a request with the default message
        request = SummaryRequest()
        print(f"Testing with message: '{request.message}'")
        
        # Test the LLM factory directly
        print("Testing LLM factory...")
        response = LLMFactory.generate_text(request.message)
        print(f"Response: {response.text}")
        print(f"Provider: {response.provider}")
        print(f"Model: {response.model}")
        
        # Test the endpoint function
        print("\nTesting endpoint function...")
        summary_response = generate_summary(request)
        print(f"Summary: {summary_response.summary}")
        print(f"Provider: {summary_response.provider}")
        print(f"Model: {summary_response.model}")
        
        print("\n✅ Summary endpoint test completed successfully!")
        
    except Exception as e:
        print(f"❌ Error testing summary endpoint: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    print("Testing Summary Endpoint")
    print("=" * 30)
    
    # Check if GEMINI_API_KEY is set
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("⚠️  GEMINI_API_KEY not set. Please set it in your .env file.")
        print("   The endpoint will work but may fail without a valid API key.")
    
    success = test_summary_endpoint()
    if success:
        print("\n🎉 All tests passed!")
    else:
        print("\n💥 Tests failed!")
        sys.exit(1) 