# Deployment Guide for Full Stack Todo App

This guide explains how to deploy your full-stack todo application to production environments.

## Architecture Overview

Your application consists of:
- **Frontend**: Next.js application (located in `/frontend` directory)
- **Backend**: FastAPI application (located in `/frontend/backend` directory)

## Deployment Strategy

Since Vercel only hosts frontend applications, you'll need to deploy your backend separately and configure your frontend to proxy API requests.

### Option 1: Separate Backend Deployment (Recommended)

#### Deploy Backend to a Cloud Platform

Deploy your FastAPI backend to one of these platforms:

**On Render:**
1. Create a new Web Service
2. Connect to your GitHub repository
3. Choose Python runtime
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
6. Set environment variables:
   - `DATABASE_URL`: Your database connection string

**On Railway:**
1. Create a new project
2. Connect to your GitHub repository
3. Choose Python template
4. Set start command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
5. Configure environment variables

**On AWS Elastic Beanstalk:**
1. Prepare your application bundle
2. Upload to Elastic Beanstalk
3. Set environment variables

#### Update Vercel Configuration

Once your backend is deployed, update the `vercel.json` file with your actual backend URL:

```json
{
  "root": "frontend",
  "framework": "nextjs",
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "https://your-actual-backend-url.com/api/$1"
    }
  ],
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        },
        {
          "key": "Access-Control-Allow-Methods",
          "value": "GET, POST, PUT, DELETE, PATCH, OPTIONS"
        },
        {
          "key": "Access-Control-Allow-Headers",
          "value": "X-Requested-With, Content-Type, Accept, Authorization"
        }
      ]
    }
  ]
}
```

#### Environment Variables

In your Vercel dashboard, set these environment variables:

- `NEXT_PUBLIC_API_BASE_URL`: Your deployed backend URL (e.g., `https://your-actual-backend-url.com`)
- `NEXT_PUBLIC_BETTER_AUTH_URL`: Your deployed backend URL (e.g., `https://your-actual-backend-url.com`)

### Option 2: Using Docker with Docker Compose

If you prefer to deploy both frontend and backend together:

1. Use the provided `docker-compose.yml` file
2. Deploy to a cloud platform that supports Docker Compose (like DigitalOcean App Platform, AWS ECS, etc.)

## Deploying Frontend to Vercel

### Prerequisites
- A Vercel account
- The Vercel CLI installed (`npm i -g vercel`)
- Your backend deployed and accessible

### Steps

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Link your project to Vercel:
   ```bash
   vercel
   ```
   
3. Follow the prompts to connect your GitHub repository or upload manually

4. Set the build settings:
   - Framework Preset: Next.js
   - Root Directory: `frontend`

5. Add the environment variables mentioned above in the Vercel dashboard

6. Deploy:
   ```bash
   vercel --prod
   ```

## Environment Variables Reference

### Frontend (set in Vercel dashboard)
- `NEXT_PUBLIC_API_BASE_URL`: Base URL of your deployed backend API
- `NEXT_PUBLIC_BETTER_AUTH_URL`: Auth endpoint URL
- `NEXT_PUBLIC_BACKEND_AVAILABLE`: Set to `true`
- `BETTER_AUTH_SECRET`: Secret for authentication (generate a strong random string)

### Backend (set in your backend hosting platform)
- `DATABASE_URL`: Database connection string
- `SECRET_KEY`: Secret for JWT tokens
- `ALGORITHM`: Algorithm for JWT (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time

## Testing the Deployment

After deployment:

1. Visit your frontend URL
2. Check browser console for any errors
3. Test authentication (sign up, sign in)
4. Test creating and managing tasks
5. Verify API calls are working correctly

## Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure your backend allows requests from your frontend domain
2. **API Calls Failing**: Verify your `NEXT_PUBLIC_API_BASE_URL` is set correctly
3. **Authentication Issues**: Check that JWT secret keys match between frontend and backend
4. **Database Connection**: Ensure your backend can connect to the database in production

### Debugging Tips

- Check browser developer tools Network tab for failed API requests
- Review backend logs for error messages
- Verify all environment variables are set correctly
- Test API endpoints directly using tools like Postman

## Scaling Recommendations

1. Use a production-ready database (PostgreSQL instead of SQLite)
2. Implement caching for improved performance
3. Set up monitoring and logging
4. Use a CDN for static assets
5. Implement proper error handling and reporting