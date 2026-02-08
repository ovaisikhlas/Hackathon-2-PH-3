#!/usr/bin/env python3
"""
Test script to check if the Google API key works with specific models
"""

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def test_models():
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    print(f"Testing API key: {api_key[:10]}..." if api_key else "No API key found")
    
    # Test different models
    models_to_test = [
        "gemini-2.5-flash",
        "gemini-2.0-flash", 
        "gemini-1.5-flash",
        "gemini-1.5-pro",
        "gemini-pro"
    ]
    
    for model_name in models_to_test:
        print(f"\nTesting model: {model_name}")
        try:
            llm = ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=api_key,
                temperature=0.7
            )
            print(f"SUCCESS: Model {model_name} initialized successfully")
            
            # Try a simple test
            from langchain_core.messages import HumanMessage
            message = HumanMessage(content="Say 'Hello' in one word.")
            response = llm.invoke([message])
            print(f"SUCCESS: API call successful: {response.content}")
            
        except Exception as e:
            print(f"ERROR: Failed to use {model_name}: {str(e)}")

if __name__ == "__main__":
    test_models()