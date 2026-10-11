from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.use_cases import (
    AlunoUseCases, CursoUseCases, DisciplinaUseCases, MatriculaUseCases,
)
from app.domain.entities.user import UserRole
from app.domain.services.auth_service import AuthService
from app.infrastructure.database.session import get_db
from app.infrastructure.database.models import UserModel
from app.infrastructure.repositories import (
    AlunoRepositoryImpl, CursoRepositoryImpl, DisciplinaRepositoryImpl,
    MatriculaRepositoryImpl,
)
from app.infrastructure.security.user_manager import current_active_user


def get_curso_use_cases(session: AsyncSession = Depends(get_db)) -> CursoUseCases:
    return CursoUseCases(CursoRepositoryImpl(session))


def get_aluno_use_cases(session: AsyncSession = Depends(get_db)) -> AlunoUseCases:
    return AlunoUseCases(AlunoRepositoryImpl(session), CursoRepositoryImpl(session))


def get_disciplina_use_cases(session: AsyncSession = Depends(get_db)) -> DisciplinaUseCases:
    return DisciplinaUseCases(
        DisciplinaRepositoryImpl(session), CursoRepositoryImpl(session)
    )


def get_matricula_use_cases(session: AsyncSession = Depends(get_db)) -> MatriculaUseCases:
    return MatriculaUseCases(
        MatriculaRepositoryImpl(session),
        AlunoRepositoryImpl(session),
        DisciplinaRepositoryImpl(session),
    )


class RoleChecker:
    def __init__(self, allowed_roles: list[UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: UserModel = Depends(current_active_user)) -> UserModel:
        AuthService.ensure_role(user.role, self.allowed_roles)
        return user


requer_coordenador = RoleChecker([UserRole.COORDENADOR])
requer_professor = RoleChecker([UserRole.PROFESSOR])
requer_professor_ou_coordenador = RoleChecker(
    [UserRole.PROFESSOR, UserRole.COORDENADOR]
)
