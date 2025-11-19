# -*- coding: utf-8 -*-
from starlette.requests import Request
from starlette.responses import JSONResponse
from asyncpg.exceptions import PostgresError


class DBErrorMiddleware:
    async def __call__(self, request: Request, call_next):
        print(f"[Middleware] Request: {request.method} {request.url}")

        try:
            response = await call_next(request)
            return response

        except PostgresError as e:
            print("[Middleware] Database error:", str(e))
            return JSONResponse(
                {"detail": "Database error occurred"},
                status_code=500
            )

        except Exception as e:
            print("[Middleware] Unexpected error:", str(e))
            return JSONResponse(
                {"detail": "Internal server error"},
                status_code=500
            )
