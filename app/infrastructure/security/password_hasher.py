from fastapi_users.password import PasswordHelper

password_helper = PasswordHelper()

class PasswordHasher:
    """Adaptador simples da estratégia de hashing padrão do FastAPI Users."""

    def hash(self, password: str) -> str:
        return password_helper.hash(password)

    def verify_and_update(self, plain_password: str, hashed_password: str):
        return password_helper.verify_and_update(plain_password, hashed_password)
