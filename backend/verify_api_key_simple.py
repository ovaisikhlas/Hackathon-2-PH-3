#!/usr/bin/env python3
"""
Script to verify if the Google API key is valid
"""

import os
import requests
from dotenv import load_dotenv

def verify_api_key():
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    print("[INFO] Verifying Google API Key...")
    print(f"API Key loaded: {'Yes' if api_key else 'No'}")
    
    if not api_key:
        print("[ERROR] No API key found in .env file")
        print("   Please add GOOGLE_API_KEY=your_actual_key to your .env file")
        return False
    
    print(f"API Key preview: {api_key[:10]}{'*' * (len(api_key)-10) if len(api_key) > 10 else ''}")
    
    # Check basic format
    if not api_key.startswith("AIza"):
        print("[ERROR] Invalid API key format")
        print("   Google API keys must start with 'AIza'")
        return False
    
    if len(api_key) < 30:
        print("[ERROR] API key appears too short")
        print("   Valid Google API keys are typically 39 characters long")
        return False
    
    print(f"[SUCCESS] Basic format check passed")
    print(f"   - Starts with 'AIza': Yes")
    print(f"   - Length: {len(api_key)} characters")
    
    # Try to make a test request to Google's API
    print("\n[INFO] Testing connection to Google API...")
    try:
        # Try to list models (this doesn't cost tokens)
        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print("[SUCCESS] Successfully connected to Google API")
            data = response.json()
            if 'models' in data and len(data['models']) > 0:
                print(f"[SUCCESS] Found {len(data['models'])} available models")
                # Show a few model names
                model_names = [model['name'] for model in data['models'][:3]]
                print(f"   Sample models: {model_names}")
                return True
            else:
                print("[WARNING] Connected but no models returned")
                return False
        elif response.status_code == 400:
            error_data = response.json()
            if 'error' in error_data and 'details' in error_data['error']:
                details = error_data['error']['details'][0]
                if details.get('@type') == 'type.googleapis.com/google.rpc.ErrorInfo':
                    reason = details.get('reason', '')
                    if reason == 'API_KEY_INVALID':
                        print("[ERROR] API key is invalid")
                        return False
            print(f"[ERROR] API request failed with status {response.status_code}")
            print(f"   Error: {error_data}")
            return False
        elif response.status_code == 403:
            print("[ERROR] API key is valid but access is forbidden")
            print("   This could mean:")
            print("   - The API is not enabled for your project")
            print("   - Billing is not set up")
            print("   - The key has restrictions")
            return False
        else:
            print(f"[ERROR] API request failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except ImportError:
        print("[WARNING] Required library 'requests' not installed")
        print("   Run: pip install requests")
        return False
    except requests.exceptions.Timeout:
        print("[ERROR] Request timed out - unable to reach Google API")
        return False
    except Exception as e:
        print(f"[ERROR] Error testing API key: {str(e)}")
        return False

if __name__ == "__main__":
    print("="*50)
    print("GOOGLE API KEY VERIFICATION")
    print("="*50)
    
    is_valid = verify_api_key()
    
    print("\n" + "="*50)
    if is_valid:
        print("[SUCCESS] API KEY IS VALID AND ACCESSIBLE!")
        print("You should be able to use Gemini models")
    else:
        print("[ERROR] API KEY IS NOT WORKING")
        print("\nTroubleshooting steps:")
        print("1. Verify the API key at https://makersuite.google.com/")
        print("2. Ensure the Generative Language API is enabled")
        print("3. Check that billing is set up for your Google Cloud project")
        print("4. Make sure the API key has proper permissions")
    print("="*50)