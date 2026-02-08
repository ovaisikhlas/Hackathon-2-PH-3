# API Configuration Guide

## Setting up Google Gemini API

To enable the AI-powered chatbot functionality, you need to configure a Google API key.

### Steps to Get Your Google API Key:

1. Visit [Google AI Studio](https://makersuite.google.com/)
2. Sign in with your Google account
3. Click on "Get API Key" or "Create API Key"
4. Follow the prompts to enable the Gemini API
5. Copy your API key

### Configuring the API Key:

1. Open the `.env` file in the backend directory
2. Replace `your_actual_google_api_key_here` with your actual API key:
   ```
   GOOGLE_API_KEY=your_copied_api_key_here
   ```
3. Save the file

### Alternative: Using Environment Variables

Instead of modifying the `.env` file, you can set the environment variable directly:

On Windows:
```cmd
set GOOGLE_API_KEY=your_api_key_here
```

On macOS/Linux:
```bash
export GOOGLE_API_KEY=your_api_key_here
```

### Testing the Configuration

After configuring your API key:

1. Restart the server
2. Send a test message to the chat endpoint
3. The AI assistant should respond with intelligent responses instead of fallback messages

### Troubleshooting

- If you still see fallback responses, verify that:
  - The API key is correctly entered in the `.env` file
  - The server has been restarted after changing the `.env` file
  - The API key has proper permissions for the Gemini API
  - Your billing is set up properly (some Google APIs require billing setup even for free tier usage)

### Without API Key

If you don't have an API key configured, the application will still run but will use fallback responses instead of AI-powered responses.