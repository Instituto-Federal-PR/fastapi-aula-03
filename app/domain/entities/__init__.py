from app.domain.entities.aluno import Aluno, AlunoResumo, MatriculaDoAluno
from app.domain.entities.curso import Curso, CursoResumo
from app.domain.entities.disciplina import (
    Disciplina,
    DisciplinaResumo,
    MatriculaDaDisciplina,
)
from app.domain.entities.matricula import Matricula
from app.domain.entities.user import UserIdentity, UserRole

__all__ = [
    "Aluno", "AlunoResumo", "Curso", "CursoResumo", "Disciplina",
    "DisciplinaResumo", "Matricula", "MatriculaDaDisciplina",
    "MatriculaDoAluno", "UserIdentity", "UserRole",
]
