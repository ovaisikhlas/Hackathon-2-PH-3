# Vercel Deployment Checklist for Todo App

## Pre-deployment Verification

### 1. Environment Variables
- [ ] `NEXT_PUBLIC_API_BASE_URL`: Set to your deployed backend URL
- [ ] `NEXT_PUBLIC_BETTER_AUTH_URL`: Set to your deployed backend URL  
- [ ] `NEXT_PUBLIC_BACKEND_AVAILABLE`: Set to `true`
- [ ] `BETTER_AUTH_SECRET`: Generate a strong random secret

### 2. Backend Deployment
- [ ] Backend API is deployed and accessible at your chosen URL
- [ ] Backend API endpoints are tested and working
- [ ] Database is configured and accessible from the backend
- [ ] CORS settings allow requests from your frontend domain

### 3. Frontend Build
- [ ] Run `npm run build` in the frontend directory locally to ensure build succeeds
- [ ] Check for any build warnings or errors
- [ ] Verify all pages and components build without issues

### 4. API Integration
- [ ] Update the destination URL in `vercel.json` with your actual backend URL
- [ ] Ensure all API routes are properly configured for production
- [ ] Test authentication flows (sign up, sign in, sign out)

### 5. Testing
- [ ] Test the deployed frontend with the backend API
- [ ] Verify all CRUD operations work correctly
- [ ] Check responsive design on different screen sizes
- [ ] Test error handling and fallback mechanisms

## Deployment Steps

1. Commit all changes to your repository
2. Push to your connected GitHub repository
3. Import the project in Vercel dashboard
4. Set the project root to `/frontend`
5. Add environment variables in Vercel dashboard
6. Deploy the project

## Post-deployment Checks

- [ ] Visit the deployed URL
- [ ] Check browser console for errors
- [ ] Test user registration and login
- [ ] Verify task creation, editing, deletion
- [ ] Test task completion toggling
- [ ] Verify all UI components render correctly
- [ ] Check that API calls are working properly

## Troubleshooting

### Common Issues:
- If API calls fail, verify the backend URL in environment variables and vercel.json
- If authentication doesn't work, check that JWT tokens are properly handled
- If styling is broken, verify that CSS is properly processed during build

### Debugging:
- Check browser network tab for failed requests
- Review Vercel deployment logs
- Verify environment variables are correctly set
- Test backend API endpoints independently