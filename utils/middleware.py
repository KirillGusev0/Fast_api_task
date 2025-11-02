# -*- coding: utf-8 -*-
from fastapi import Request
from fastapi.responses import JSONResponse
from utils.jwt import decode_token

async def jwt_middleware(request: Request, call_next):
    if request.url.path.startswith(("/auth", "/docs", "/openapi.json")):
        return await call_next(request)
    token = request.headers.get("Authorization")
    if not token:
        return JSONResponse(status_code=401, content={"error": "Missing token"})
    try:
        decode_token(token.replace("Bearer ", ""))
    except Exception as e:
        return JSONResponse(status_code=401, content={"error": str(e)})
    return await call_next(request)
