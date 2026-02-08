# backend/auth/better_auth_config.py
from better_auth import auth_backend
from better_auth.oauth.github import github_oauth  # Example OAuth provider
from better_auth.config import Config
from better_auth.transport import CookieTransport
from better_auth import BaseUser
from typing import Optional
import os

# Define a custom user model if needed
class CustomUser(BaseUser):
    def __init__(self, id: str, email: str, name: Optional[str] = None):
        super().__init__(id=id, email=email, name=name)

# Configure Better Auth
def get_better_auth_config():
    config = Config(
        secret=os.getenv("BETTER_AUTH_SECRET", "your-secret-key-change-in-production"),
        database_url=os.getenv("DATABASE_URL"),
        transport=CookieTransport(
            name="better-auth.session",
            max_age=60 * 60 * 24 * 7,  # 1 week
            secure=False,  # Set to True in production with HTTPS
            http_only=True,
            same_site="lax",
        ),
        base_path="/api/auth",  # All auth routes will be prefixed with this
        # Enable JWT if needed
        jwt_secret=os.getenv("BETTER_AUTH_SECRET"),
        jwt_algorithm="HS256",
        jwt_max_age=60 * 60 * 24 * 7,  # 1 week
    )
    
    return config

# Initialize the auth backend
auth = auth_backend(get_better_auth_config())

# Add any custom providers or configurations
# auth.add_provider(github_oauth(...))

__all__ = ["auth", "CustomUser"]