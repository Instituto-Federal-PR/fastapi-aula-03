from collections.abc import Iterable

from app.core.exceptions import Forbidden
from app.domain.entities.user import UserRole


class AuthService:
    """Política de autorização por papel, sem dependência de HTTP ou ORM."""

    @staticmethod
    def ensure_role(user_role: str | UserRole, allowed_roles: Iterable[UserRole]) -> None:
        if user_role not in allowed_roles:
            raise Forbidden()
