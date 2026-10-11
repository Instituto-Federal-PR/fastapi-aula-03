from typing import Optional
from uuid import UUID

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import RESET_PASSWORD_TOKEN_SECRET, VERIFICATION_TOKEN_SECRET
from app.infrastructure.database.session import get_db
from app.infrastructure.database.models import UserModel
from app.infrastructure.security.auth_backend import auth_backend
from app.infrastructure.security.password_hasher import password_helper


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, UserModel)


class UserManager(UUIDIDMixin, BaseUserManager[UserModel, UUID]):
    reset_password_token_secret = RESET_PASSWORD_TOKEN_SECRET
    verification_token_secret = VERIFICATION_TOKEN_SECRET
    password_helper = password_helper

    async def on_after_register(self, user: UserModel, request: Optional[Request] = None):
        print(f"Usuário {user.id} foi registrado com sucesso.")


def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


fastapi_users = FastAPIUsers[UserModel, UUID](get_user_manager, [auth_backend])
current_active_user = fastapi_users.current_user(active=True)
