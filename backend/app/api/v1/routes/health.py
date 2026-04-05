"""
Health check endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from supabase import Client
from app.core.supabase import get_supabase
from datetime import datetime
from typing import Dict, Any

router = APIRouter()


@router.get("/health")
async def health_check() -> Dict[str, Any]:
    """
    Basic health check endpoint.
    Returns API status and timestamp.
    
    Returns:
        dict: Health status information
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }


@router.get("/health/db")
async def database_health(
    supabase: Client = Depends(get_supabase)
) -> Dict[str, Any]:
    """
    Detailed database health check.
    Tests connection to all tables.
    
    Args:
        supabase: Supabase client (injected)
    
    Returns:
        dict: Database health status
    """
    try:
        # Test all tables
        tables = ["user_profiles", "dreams", "videos"]
        table_status = {}
        
        for table in tables:
            try:
                result = supabase.table(table).select("count", count="exact").execute()
                table_status[table] = {
                    "status": "ok",
                    "count": result.count
                }
            except Exception as e:
                table_status[table] = {
                    "status": "error",
                    "error": str(e)
                }
        
        # Check if all tables are OK
        all_ok = all(t["status"] == "ok" for t in table_status.values())
        
        return {
            "status": "healthy" if all_ok else "degraded",
            "timestamp": datetime.utcnow().isoformat(),
            "database": {
                "status": "connected" if all_ok else "issues_detected",
                "tables": table_status
            }
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "status": "unhealthy",
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
        )


@router.get("/health/detailed")
async def detailed_health(
    supabase: Client = Depends(get_supabase)
) -> Dict[str, Any]:
    """
    Comprehensive health check including all services.
    
    Args:
        supabase: Supabase client (injected)
    
    Returns:
        dict: Detailed health information
    """
    health_info = {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "services": {}
    }
    
    # Check database
    try:
        result = supabase.table("user_profiles").select("count", count="exact").execute()
        health_info["services"]["database"] = {
            "status": "healthy",
            "users_count": result.count
        }
    except Exception as e:
        health_info["services"]["database"] = {
            "status": "unhealthy",
            "error": str(e)
        }
        health_info["status"] = "degraded"
    
    # Check storage
    try:
        # Just verify we can initialize storage client
        from app.config import settings
        health_info["services"]["storage"] = {
            "status": "configured",
            "bucket": settings.STORAGE_BUCKET_THUMBNAILS
        }
    except Exception as e:
        health_info["services"]["storage"] = {
            "status": "error",
            "error": str(e)
        }
    
    # AI Services status (just config check for now)
    from app.config import settings
    health_info["services"]["ai"] = {
        "anthropic": "configured" if settings.ANTHROPIC_API_KEY else "not_configured",
        "runway": "configured" if settings.RUNWAY_API_KEY else "not_configured"
    }
    
    return health_info