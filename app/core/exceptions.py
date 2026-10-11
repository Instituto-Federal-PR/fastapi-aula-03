class ApplicationError(Exception):
    """Erro de aplicação traduzido na borda HTTP."""

    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class NotFound(ApplicationError):
    def __init__(self, message: str):
        super().__init__(message, 404)


class InvalidReference(ApplicationError):
    def __init__(self, message: str):
        super().__init__(message, 400)


class Forbidden(ApplicationError):
    def __init__(self, message: str = "Você não tem permissão para executar esta ação."):
        super().__init__(message, 403)
