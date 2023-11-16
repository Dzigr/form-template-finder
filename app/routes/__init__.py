from fastapi import APIRouter

from .forms import router as form_router

v1 = APIRouter(prefix='/api/v1')
v1.include_router(form_router)

__all__ = (v1, )
