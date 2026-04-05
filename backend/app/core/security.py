"""
Security utilities for authentication and authorization
"""

from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.config import settings


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    
    Args:
        plain_password: Plain text password
        hashed_password: Hashed password from database
    
    Returns:
        bool: True if password matches, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hash a password.
    
    Args:
        password: Plain text password
    
    Returns:
        str: Hashed password
    """
    return pwd_context.hash(password)


def create_access_token(
    data: Dict[str, Any],
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create a JWT access token.
    
    Note: In production with Supabase, we use Supabase's built-in JWT.
    This is for local testing or custom token generation if needed.
    
    Args:
        data: Data to encode in the token
        expires_delta: Token expiration time
    
    Returns:
        str: Encoded JWT token
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    to_encode.update({"exp": expire})
    
    # Use Supabase JWT secret if available, otherwise use custom
    secret = settings.JWT_SECRET if settings.JWT_SECRET else "fallback-secret-key"
    
    encoded_jwt = jwt.encode(
        to_encode,
        secret,
        algorithm=settings.JWT_ALGORITHM
    )
    
    return encoded_jwt


def verify_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Verify and decode a JWT token.
    
    Args:
        token: JWT token string
    
    Returns:
        Optional[Dict]: Decoded token data or None if invalid
    """
    try:
        secret = settings.JWT_SECRET if settings.JWT_SECRET else "fallback-secret-key"
        payload = jwt.decode(
            token,
            secret,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except JWTError:
        return None


# Convenience exports
__all__ = [
    "verify_password",
    "get_password_hash",
    "create_access_token",
    "verify_token"
]