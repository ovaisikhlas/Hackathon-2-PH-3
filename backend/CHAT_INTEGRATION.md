# Chat Endpoint Integration Guide

## Backend Endpoint

The AI-powered chat endpoint is available at:
```
POST /api/{user_id}/chat
```

### Request Format
```json
{
  "message": "Your message to the AI assistant",
  "conversation_id": "optional conversation ID to continue an existing conversation"
}
```

### Response Format
```json
{
  "response": "AI-generated response",
  "conversation_id": "ID of the conversation (new or existing)"
}
```

### Authentication
- Requires Bearer token authentication in the Authorization header
- Token should be obtained from the login endpoint (`/api/auth/sign-in/credentials`)

## Frontend Integration Example

Here's how to integrate the chat endpoint with your frontend:

### Using fetch API:
```javascript
const chatWithAI = async (userId, message, conversationId = null) => {
  try {
    const response = await fetch(`/api/${userId}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // or however you store the token
      },
      body: JSON.stringify({
        message: message,
        conversation_id: conversationId
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error chatting with AI:', error);
    throw error;
  }
};
```

### Example Usage:
```javascript
// Start a new conversation
const result = await chatWithAI('user-123', 'What are my tasks?');

// Continue an existing conversation
const continuedResult = await chatWithAI('user-123', 'Mark the first task as complete', result.conversation_id);
```

## Features

The AI assistant can help with:
- Adding new tasks
- Listing all tasks
- Marking tasks as complete
- Deleting tasks
- Updating tasks

## Error Handling

Common error responses:
- `401 Unauthorized`: Invalid or missing authentication token
- `403 Forbidden`: User is not authorized to access this resource
- `404 Not Found`: Conversation not found
- `500 Internal Server Error`: Server-side error processing the request

## Testing

You can test the endpoint using the test script:
```bash
python test_endpoints.py
```