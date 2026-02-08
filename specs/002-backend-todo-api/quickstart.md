# Backend Todo API - Quickstart Guide

## Overview
This quickstart guide provides instructions for setting up and running the Todo API backend quickly.

## Prerequisites
- Python 3.8 or higher
- pip package manager
- Neon PostgreSQL database (or local PostgreSQL instance)
- Better Auth configured for JWT tokens

## Setup Instructions

### 1. Clone or Navigate to Backend Directory
```bash
cd C:\Users\Ovais\Desktop\Hackathon II Ph#2  Full Stack Todo App Frontend\backend
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create Environment File
Create a `.env` file in the backend directory with the following content:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/todoapp
BETTER_AUTH_SECRET=your-super-secret-key-change-in-production
SECRET_KEY=your-secret-key
ENVIRONMENT=development
```

### 5. Initialize Database Tables
Run the table creation script:
```bash
python create_tables.py
```

### 6. Start the Backend Server
```bash
python start_server.py
# Or alternatively: uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at `http://localhost:8000`

## API Endpoints

### Authentication Required
All endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer {jwt_token}
```

### Available Endpoints
- `GET /api/{user_id}/tasks` - List all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion
- `GET /health` - Health check endpoint

## Testing the API

### Using cURL (with example token)
```bash
curl -H "Authorization: Bearer your-jwt-token-here" \
     -H "Content-Type: application/json" \
     http://localhost:8000/api/user123/tasks
```

### Using Swagger UI
Visit `http://localhost:8000/docs` for interactive API documentation and testing.

## Environment Variables
- `DATABASE_URL`: PostgreSQL connection string
- `BETTER_AUTH_SECRET`: Secret key for JWT verification
- `SECRET_KEY`: General secret key for encryption
- `ENVIRONMENT`: Environment setting (development/production)

## Troubleshooting

### Common Issues
1. **Database Connection Error**: Verify DATABASE_URL is correct
2. **JWT Authentication Error**: Ensure BETTER_AUTH_SECRET matches the one used by Better Auth
3. **CORS Errors**: Check if frontend origin is allowed in CORS configuration

### Health Check
Verify the backend is running:
```bash
curl http://localhost:8000/health
```

## Stopping the Server
Press `Ctrl+C` in the terminal where the server is running.