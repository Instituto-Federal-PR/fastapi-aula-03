from fastapi import APIRouter

from app.infrastructure.security.auth_backend import auth_backend
from app.infrastructure.security.user_manager import fastapi_users
from app.presentation.schemas.user_schemas import UserCreate, UserRead

router = APIRouter()
router.include_router(
    fastapi_users.get_auth_router(auth_backend), 
    prefix="/auth/jwt", tags=["Auth"]
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate), 
    prefix="/auth", tags=["Auth"]
)
