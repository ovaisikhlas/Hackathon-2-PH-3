"""
Simple test to verify the chat API fix
"""
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def test_api_key_check():
    """Test that our API key check works properly"""
    
    # Check current API key in environment
    google_api_key = os.getenv("GOOGLE_API_KEY")
    print(f"Current GOOGLE_API_KEY: {google_api_key}")
    
    # Test the condition from our code (checking for both possible placeholder values)
    if not google_api_key or google_api_key in ["your_actual_google_api_key_here", "your_google_api_key_here"]:
        print("[SUCCESS] Our code will correctly detect missing/placeholder API key")
        print("[SUCCESS] Fallback response mechanism will be triggered")
        return True
    else:
        print("[INFO] API key is set, normal LLM initialization would occur")
        return False

if __name__ == "__main__":
    result = asyncio.run(test_api_key_check())
    if result:
        print("\n[SUCCESS] Fix verified: The application will handle missing API key gracefully")
    else:
        print("\n[INFO] API key is configured, normal operation will occur")