#!/usr/bin/env python3
"""
Script to verify if the Google API key is valid
"""

import os
import asyncio
from dotenv import load_dotenv

def verify_api_key():
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    print("🔍 Verifying Google API Key...")
    print(f"API Key loaded: {'Yes' if api_key else 'No'}")
    
    if not api_key:
        print("❌ ERROR: No API key found in .env file")
        print("   Please add GOOGLE_API_KEY=your_actual_key to your .env file")
        return False
    
    print(f"API Key preview: {api_key[:10]}{'*' * (len(api_key)-10) if len(api_key) > 10 else ''}")
    
    # Check basic format
    if not api_key.startswith("AIza"):
        print("❌ ERROR: Invalid API key format")
        print("   Google API keys must start with 'AIza'")
        return False
    
    if len(api_key) < 30:
        print("❌ ERROR: API key appears too short")
        print("   Valid Google API keys are typically 39 characters long")
        return False
    
    print(f"✅ Basic format check passed")
    print(f"   - Starts with 'AIza': Yes")
    print(f"   - Length: {len(api_key)} characters")
    
    # Try to make a test request to Google's API
    print("\n📡 Testing connection to Google API...")
    try:
        import google.generativeai as genai
        
        # Configure the API
        genai.configure(api_key=api_key)
        
        # Try to list models (this doesn't cost tokens)
        import requests
        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            print("✅ Successfully connected to Google API")
            data = response.json()
            if 'models' in data and len(data['models']) > 0:
                print(f"✅ Found {len(data['models'])} available models")
                # Show a few model names
                model_names = [model['name'] for model in data['models'][:3]]
                print(f"   Sample models: {model_names}")
                return True
            else:
                print("⚠️  Connected but no models returned")
                return False
        elif response.status_code == 400:
            error_data = response.json()
            if 'error' in error_data and 'details' in error_data['error']:
                details = error_data['error']['details'][0]
                if details.get('@type') == 'type.googleapis.com/google.rpc.ErrorInfo':
                    reason = details.get('reason', '')
                    if reason == 'API_KEY_INVALID':
                        print("❌ ERROR: API key is invalid")
                        return False
            print(f"❌ API request failed with status {response.status_code}")
            print(f"   Error: {error_data}")
            return False
        elif response.status_code == 403:
            print("❌ ERROR: API key is valid but access is forbidden")
            print("   This could mean:")
            print("   - The API is not enabled for your project")
            print("   - Billing is not set up")
            print("   - The key has restrictions")
            return False
        else:
            print(f"❌ API request failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except ImportError:
        print("⚠️  Google API libraries not installed")
        print("   Run: pip install google-generativeai requests")
        return False
    except Exception as e:
        print(f"❌ Error testing API key: {str(e)}")
        return False

if __name__ == "__main__":
    print("="*50)
    print("GOOGLE API KEY VERIFICATION")
    print("="*50)
    
    is_valid = verify_api_key()
    
    print("\n" + "="*50)
    if is_valid:
        print("🎉 API KEY IS VALID AND ACCESSIBLE!")
        print("✅ You should be able to use Gemini models")
    else:
        print("❌ API KEY IS NOT WORKING")
        print("\nTroubleshooting steps:")
        print("1. Verify the API key at https://makersuite.google.com/")
        print("2. Ensure the Generative Language API is enabled")
        print("3. Check that billing is set up for your Google Cloud project")
        print("4. Make sure the API key has proper permissions")
    print("="*50)