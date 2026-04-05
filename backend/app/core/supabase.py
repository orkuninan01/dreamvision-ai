"""
Supabase Client Configuration
Provides Supabase client instances for database operations
"""

from supabase import create_client, Client
from app.config import settings
from functools import lru_cache
from typing import Optional
import httpx


@lru_cache()
def get_supabase_client() -> Client:
    """
    Create and cache Supabase client with SERVICE_KEY.
    
    Uses SERVICE_KEY for backend operations (bypasses RLS).
    This is the admin client - use with caution!
    
    Returns:
        Client: Supabase client instance
    """
    # Create client without proxy parameter
    client = create_client(
        supabase_url=settings.SUPABASE_URL,
        supabase_key=settings.SUPABASE_SERVICE_KEY
    )
    return client


def get_supabase_anon_client() -> Client:
    """
    Create Supabase client with ANON_KEY.
    
    Uses ANON_KEY which respects Row Level Security (RLS) policies.
    Use this for user-scoped operations where you want RLS to apply.
    
    Returns:
        Client: Supabase client instance with RLS enabled
    """
    client = create_client(
        supabase_url=settings.SUPABASE_URL,
        supabase_key=settings.SUPABASE_ANON_KEY
    )
    return client


async def get_supabase() -> Client:
    """
    Dependency for FastAPI routes.
    Returns the cached admin client (SERVICE_KEY).
    
    Usage in FastAPI:
        @app.get("/endpoint")
        async def endpoint(supabase: Client = Depends(get_supabase)):
            result = supabase.table("users").select("*").execute()
    
    Returns:
        Client: Supabase admin client
    """
    return get_supabase_client()


def test_connection() -> bool:
    """
    Test Supabase connection.
    
    Returns:
        bool: True if connection successful, False otherwise
    """
    try:
        client = get_supabase_client()
        # Try a simple query
        result = client.table("user_profiles").select("id").limit(1).execute()
        print(f"✅ Connection successful! Found {len(result.data)} records")
        return True
    except Exception as e:
        print(f"❌ Supabase connection failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


# Convenience exports
__all__ = [
    "get_supabase_client",
    "get_supabase_anon_client", 
    "get_supabase",
    "test_connection"
]