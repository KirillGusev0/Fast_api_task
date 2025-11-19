# -*- coding: utf-8 -*-
import jwt
from datetime import datetime, timedelta
from settings.settings import settings


def create_access_token(data: dict) -> str:
    
    payload = {
        "sub": data["sub"],
        "user_id": data["user_id"],
        "type": "access",
        "exp": datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRE_MINUTES),
        "iat": datetime.utcnow(),
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGO)


def create_refresh_token(data: dict) -> str:
    
    payload = {
        "sub": data["sub"],
        "user_id": data["user_id"],
        "type": "refresh",
        "exp": datetime.utcnow() + timedelta(hours=1),   
        "iat": datetime.utcnow(),
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGO)


def decode_token(token: str) -> dict:
    
    try:
        return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGO])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

