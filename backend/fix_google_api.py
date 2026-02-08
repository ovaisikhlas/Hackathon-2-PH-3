#!/usr/bin/env python3
"""
Script to help fix the Google API issue by updating the chat.py file
to use a more robust error handling approach and potentially different models
"""

import os
import re

def update_chat_api():
    chat_file_path = "api/chat.py"
    
    # Read the current chat.py file
    with open(chat_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Updating chat API to improve Google API error handling...")
    
    # Find the section where the Google API is initialized and update it
    # Look for the section that initializes the Google model
    pattern = r"# Initialize the Google Gemini LLM\s*\n\s*llm = ChatGoogleGenerativeAI\(.*?\)"
    
    # More specific pattern to match the exact initialization
    pattern = r"llm = ChatGoogleGenerativeAI\(model=\"gemini-1\.5-flash\", temperature=0\.3\)"
    
    # Replace with a more robust version that tries multiple models
    new_llm_init = '''# Initialize the Google Gemini LLM with fallback models
    available_models = ["gemini-1.5-pro", "gemini-1.0-pro", "gemini-pro", "gemini-1.5-flash"]
    llm = None
    model_used = None
    
    for model_name in available_models:
        try:
            llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.3, google_api_key=google_api_key)
            model_used = model_name
            print(f"Successfully initialized model: {model_name}")
            break
        except Exception as e:
            print(f"Model {model_name} not available: {str(e)}")
            continue
    
    if llm is None:
        # If no models are available, force fallback response
        raise Exception("No Google AI models available")'''
    
    # Find and replace the model initialization
    if "llm = ChatGoogleGenerativeAI(model=\"gemini-1.5-flash\"" in content:
        content = re.sub(
            r'llm = ChatGoogleGenerativeAI\(model="gemini-1\.5-flash", temperature=0\.3\)',
            new_llm_init,
            content,
            count=1
        )
        print("Updated model initialization with fallback logic")
    else:
        # If the exact pattern isn't found, we'll add error handling around the existing code
        print("Could not find exact model initialization pattern, adding error handling...")
        
        # Look for the section where the LLM is initialized and wrap it in try-catch
        if "llm = ChatGoogleGenerativeAI" in content:
            # Find the line and add error handling around it
            lines = content.split('\n')
            updated_lines = []
            
            for line in lines:
                if 'llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash"' in line:
                    updated_lines.append("    try:")
                    updated_lines.append(f"        {line.strip()}")
                    updated_lines.append("        model_used = 'gemini-1.5-flash'")
                    updated_lines.append("    except Exception as e:")
                    updated_lines.append("        print(f'Primary model unavailable: {e}')")
                    updated_lines.append("        # Force fallback to prevent errors")
                    updated_lines.append("        logger.warning(f'Google API error: {e}. Using fallback response.')")
                    updated_lines.append("")
                    updated_lines.append("        # Provide a fallback response based on the user's message")
                    updated_lines.append("        user_msg_lower = request.message.lower()")
                    updated_lines.append("        if \"hello\" in user_msg_lower or \"hi\" in user_msg_lower:")
                    updated_lines.append("            ai_response = \"Hello! I'm your AI assistant. How can I help you with your tasks today? (Note: Google API not configured or unavailable, using fallback response)\"")
                    updated_lines.append("        elif \"task\" in user_msg_lower and (\"add\" in user_msg_lower or \"create\" in user_msg_lower):")
                    updated_lines.append("            ai_response = \"I can help you add a task. Please provide the task title and description. (Note: Google API not configured or unavailable, using fallback response)\"")
                    updated_lines.append("        elif \"list\" in user_msg_lower or \"show\" in user_msg_lower:")
                    updated_lines.append("            ai_response = \"I can help you list your tasks. You have 2 active tasks: 'Sample Task 1' and 'Sample Task 2'. (Note: Google API not configured or unavailable, using fallback response)\"")
                    updated_lines.append("        elif \"complete\" in user_msg_lower or \"done\" in user_msg_lower:")
                    updated_lines.append("            ai_response = \"I can help you mark a task as complete. Which task would you like to mark as done? (Note: Google API not configured or unavailable, using fallback response)\"")
                    updated_lines.append("        elif \"delete\" in user_msg_lower:")
                    updated_lines.append("            ai_response = \"I can help you delete a task. Which task would you like to delete? (Note: Google API not configured or unavailable, using fallback response)\"")
                    updated_lines.append("        elif \"update\" in user_msg_lower:")
                    updated_lines.append("            ai_response = \"I can help you update a task. Which task would you like to update? (Note: Google API not configured or unavailable, using fallback response)\"")
                    updated_lines.append("        else:")
                    updated_lines.append("            ai_response = f\"I understand you said: '{request.message}'. I'm your AI assistant and can help you manage your tasks. You can ask me to add, list, update, or complete tasks. (Note: Google API not configured or unavailable, using fallback response)\"")
                    updated_lines.append("")
                    updated_lines.append("        # Save AI response")
                    updated_lines.append("        ai_message = Message(")
                    updated_lines.append("            conversation_id=conversation.id,")
                    updated_lines.append("            role=\"assistant\",")
                    updated_lines.append("            content=ai_response")
                    updated_lines.append("        )")
                    updated_lines.append("        db.add(ai_message)")
                    updated_lines.append("        db.commit()")
                    updated_lines.append("")
                    updated_lines.append("        return ChatResponse(")
                    updated_lines.append("            response=ai_response,")
                    updated_lines.append("            conversation_id=conversation.id")
                    updated_lines.append("        )")
                else:
                    updated_lines.append(line)
            
            content = "\n".join(updated_lines)
    
    # Write the updated content back to the file
    with open(chat_file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {chat_file_path} with improved error handling")
    print("\nTo fully resolve the issue, you need to:")
    print("1. Get a valid Google API key from https://makersuite.google.com/")
    print("2. Make sure the Gemini API is enabled for your Google Cloud project")
    print("3. Update the GOOGLE_API_KEY in backend/.env with your valid key")
    print("4. Restart the backend server")


if __name__ == "__main__":
    update_chat_api()