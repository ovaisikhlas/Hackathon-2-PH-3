#!/usr/bin/env python3
"""
Simple test script to debug the password hashing issue.
"""

from passlib.context import CryptContext
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize password context (same as in auth.py)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__ident="2b")

def get_password_hash(password: str) -> str:
    """
    Hash a password with bcrypt, ensuring it's under 72 bytes.
    """
    print(f"Input password: '{password}'")
    print(f"Input password length: {len(password)}")
    print(f"Input password byte length: {len(password.encode('utf-8'))}")
    
    # Ensure the password is definitely under 72 bytes for bcrypt
    # First, encode to bytes
    password_bytes = password.encode('utf-8')
    print(f"Encoded bytes length: {len(password_bytes)}")

    # Truncate to exactly 72 bytes if needed
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
        logging.info(f"Password truncated from {len(password.encode('utf-8'))} to {len(password_bytes)} bytes for bcrypt compatibility")

    # Decode back to string, handling any potential issues with incomplete characters
    safe_password = password_bytes.decode('utf-8', errors='ignore')
    print(f"Decoded safe password: '{safe_password}'")
    print(f"Safe password length: {len(safe_password)}")
    print(f"Safe password byte length: {len(safe_password.encode('utf-8'))}")

    # Double-check the length to ensure it's definitely under 72 bytes
    if len(safe_password.encode('utf-8')) > 72:
        # If somehow the decoded string is still too long, truncate by characters
        safe_password = safe_password[:72]
        # And double-check the byte length again
        safe_bytes = safe_password.encode('utf-8')[:72]
        safe_password = safe_bytes.decode('utf-8', errors='ignore')
        print(f"After second truncation: '{safe_password}'")

    try:
        print(f"About to hash password: '{safe_password}'")
        print(f"Final password byte length: {len(safe_password.encode('utf-8'))}")
        hashed = pwd_context.hash(safe_password)
        logging.info(f"Password hashed successfully")
        return hashed
    except ValueError as ve:
        # If we still get the bcrypt error, log it and raise
        logging.error(f"Bcrypt error despite truncation: {ve}")
        raise
    except Exception as e:
        logging.error(f"Error during password hashing: {e}")
        raise

# Test the function
if __name__ == "__main__":
    try:
        test_password = "password123"
        print(f"Testing password: {test_password}")
        hashed = get_password_hash(test_password)
        print(f"Hashed password: {hashed}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()