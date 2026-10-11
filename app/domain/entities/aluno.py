from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from app.domain.entities.curso import CursoResumo

if TYPE_CHECKING:
    from app.domain.entities.disciplina import DisciplinaResumo


@dataclass(frozen=True)
class AlunoResumo:
    id: int
    nome: str
    turma: int
    curso_id: int | None = None


@dataclass(frozen=True)
class MatriculaDoAluno:
    aluno_id: int
    disciplina_id: int
    disciplina: Optional["DisciplinaResumo"] = None


@dataclass(frozen=True)
class Aluno:
    id: int
    nome: str
    turma: int
    curso_id: int
    criado_em: datetime
    alterado_em: datetime
    curso: CursoResumo
    matricula: list[MatriculaDoAluno] = field(default_factory=list)
