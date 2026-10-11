from typing import Optional
from uuid import UUID

from fastapi_users import schemas
from pydantic import ConfigDict

from app.domain.entities.user import UserRole


class UserRead(schemas.BaseUser[UUID]):
    role: UserRole
    model_config = ConfigDict(from_attributes=True)


class UserCreate(schemas.BaseUserCreate):
    role: UserRole = UserRole.PROFESSOR


class UserUpdate(schemas.BaseUserUpdate):
    role: Optional[UserRole] = None
