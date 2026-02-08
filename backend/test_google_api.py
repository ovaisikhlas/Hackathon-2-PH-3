#!/usr/bin/env python3
"""
Test script to verify Google API functionality independently
"""

import os
from dotenv import load_dotenv
load_dotenv()

def test_google_api():
    print("Testing Google API connection...")
    
    # Get the API key
    api_key = os.getenv('GOOGLE_API_KEY')
    print(f"API Key loaded: {bool(api_key)}")
    
    if not api_key:
        print("ERROR: No API key found in environment")
        return False
    
    # Clean the API key (remove quotes if present)
    clean_api_key = api_key.strip('"\'')
    print(f"Clean API key: {clean_api_key[:10]}..." if clean_api_key else "None")
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        from langchain_core.messages import HumanMessage
        
        print("Initializing Google Generative AI model...")
        
        # Initialize the model - try gemini-pro first as it's more commonly available
        try:
            llm = ChatGoogleGenerativeAI(
                model="gemini-1.0-pro",
                temperature=0.3,
                google_api_key=clean_api_key  # Pass the key explicitly
            )
            model_name = "gemini-1.0-pro"
        except Exception as model_error:
            print(f"gemini-1.0-pro not available: {model_error}")
            print("Trying gemini-pro...")
            try:
                llm = ChatGoogleGenerativeAI(
                    model="gemini-pro",
                    temperature=0.3,
                    google_api_key=clean_api_key
                )
                model_name = "gemini-pro"
            except Exception as model_error2:
                print(f"gemini-pro also not available: {model_error2}")
                print("Trying gemini-1.5-flash again...")
                llm = ChatGoogleGenerativeAI(
                    model="gemini-1.5-flash",
                    temperature=0.3,
                    google_api_key=clean_api_key  # Pass the key explicitly
                )
                model_name = "gemini-1.5-flash"
        
        print(f"Model {model_name} initialized successfully. Testing API call...")
        
        # Test with a simple message
        message = HumanMessage(content="Say 'Hello' in one word.")
        response = llm.invoke([message])
        
        print(f"API call successful! Response: {response.content}")
        return True
        
    except ImportError as e:
        print(f"Import error - missing dependencies: {e}")
        print("You may need to install required packages: pip install langchain-google-genai google-generativeai")
        return False
    except Exception as e:
        print(f"Error with Google API: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_google_api()
    if success:
        print("\n✓ Google API is working correctly!")
    else:
        print("\n✗ Google API is not working. This explains why fallback responses are being used.")