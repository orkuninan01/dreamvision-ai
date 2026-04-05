"""
Application Configuration
Manages environment variables and settings
"""

from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables
    """
    
    # ================================
    # API Configuration
    # ================================
    API_VERSION: str = "v1"
    API_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "DreamVision AI"
    ENVIRONMENT: str = "development"  # development | staging | production
    
    # ================================
    # Server Configuration
    # ================================
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # ================================
    # Supabase Configuration
    # ================================
    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str
    SUPABASE_SERVICE_KEY: str
    
    # ================================
    # AI Services
    # ================================
    ANTHROPIC_API_KEY: str
    RUNWAY_API_KEY: str
    
    # ================================
    # CORS Configuration
    # ================================
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:19006",  # Expo default
        "http://localhost:8081",   # Expo alternative
        "exp://localhost:19000",   # Expo deep link
        "http://localhost:3000",   # Web (future)
    ]
    
    # ================================
    # Rate Limiting
    # ================================
    RATE_LIMIT_PER_MINUTE: int = 10
    
    # ================================
    # Logging
    # ================================
    LOG_LEVEL: str = "INFO"  # DEBUG | INFO | WARNING | ERROR
    
    # ================================
    # Storage
    # ================================
    STORAGE_BUCKET_THUMBNAILS: str = "video-thumbnails"
    STORAGE_PUBLIC_URL: str = ""  # Will be set from SUPABASE_URL
    
    # ================================
    # JWT Configuration (Supabase managed)
    # ================================
    JWT_SECRET: str = ""  # Optional, Supabase handles this
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    class Config:
        """Pydantic config"""
        env_file = ".env"
        case_sensitive = True
        extra = "allow"  # Allow extra fields
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Auto-construct storage public URL from Supabase URL
        if not self.STORAGE_PUBLIC_URL and self.SUPABASE_URL:
            self.STORAGE_PUBLIC_URL = f"{self.SUPABASE_URL}/storage/v1/object/public"


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance
    Using lru_cache to avoid re-reading .env on every call
    """
    return Settings()


# Global settings instance
settings = get_settings()


# ================================
# Convenience exports
# ================================
__all__ = ["settings", "get_settings", "Settings"]