from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.config import settings
from app.middleware.request_validator import RequestBodyValidationMiddleware
from app.routes import v1

app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs", debug=True)

app.include_router(v1)

origins = ["*"]

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
)

app.add_middleware(RequestBodyValidationMiddleware)


@app.get("/api/ping")
async def ping():
    return "pong"

