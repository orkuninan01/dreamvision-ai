"""
DreamVision AI - FastAPI Backend
Main application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import logging

from app.config import settings
from app.api.v1.routes import health

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    description="AI-powered dream to video generation API",
    openapi_url=f"{settings.API_PREFIX}/openapi.json",
    docs_url=f"{settings.API_PREFIX}/docs",
    redoc_url=f"{settings.API_PREFIX}/redoc",
)

# Add rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    health.router,
    prefix=settings.API_PREFIX,
    tags=["Health"]
)

# Future routers will be added here:
# app.include_router(auth.router, prefix=settings.API_PREFIX, tags=["Authentication"])
# app.include_router(dreams.router, prefix=settings.API_PREFIX, tags=["Dreams"])
# app.include_router(videos.router, prefix=settings.API_PREFIX, tags=["Videos"])


@app.on_event("startup")
async def startup_event():
    """
    Run on application startup
    """
    logger.info(f"🚀 Starting {settings.PROJECT_NAME}")
    logger.info(f"📍 Environment: {settings.ENVIRONMENT}")
    logger.info(f"🔗 API Prefix: {settings.API_PREFIX}")
    logger.info(f"📖 Docs available at: {settings.API_PREFIX}/docs")
    
    # Test Supabase connection
    try:
        from app.core.supabase import test_connection
        connected = test_connection()
        if connected:
            logger.info("✅ Supabase connection successful")
        else:
            logger.warning("⚠️ Supabase connection failed")
    except Exception as e:
        logger.error(f"❌ Supabase connection error: {e}")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Run on application shutdown
    """
    logger.info(f"👋 Shutting down {settings.PROJECT_NAME}")


@app.get("/")
async def root():
    """
    Root endpoint - API information
    """
    return {
        "message": "DreamVision AI API",
        "version": settings.API_VERSION,
        "environment": settings.ENVIRONMENT,
        "docs": f"{settings.API_PREFIX}/docs",
        "health": f"{settings.API_PREFIX}/health"
    }


# Run with: uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
        log_level=settings.LOG_LEVEL.lower()
    )