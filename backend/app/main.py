from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.tasks import router
from api.auth import router as auth_router
from api.chat import router as chat_router
from core.config import settings
from database.database import create_db_and_tables

def create_app():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

    #origins = [
    #http://localhost:3000",  # Common React port
    #"http://localhost:5173",  # Common Vite port
    #"http://127.0.0.1:3000",
    ##]

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],#origins, #["*"],#settings.ALLOWED_ORIGINS,  # Use the configured allowed origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Create database tables
    create_db_and_tables()

    # Include API routes
    app.include_router(router, prefix="/api/{user_id}", tags=["tasks"])
    app.include_router(auth_router, prefix="/api", tags=["auth"])
    app.include_router(chat_router, prefix="/api", tags=["chat"])

    # Note: Better Auth integration would typically be added here
    # For now, we'll continue with our custom JWT implementation
    # which follows the same patterns as Better Auth

    @app.get("/")
    def read_root():
        return {"message": "Todo App Backend - Phase III: AI Chatbot Integration"}

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)