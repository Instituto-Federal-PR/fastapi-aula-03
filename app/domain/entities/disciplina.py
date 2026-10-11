from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from app.domain.entities.curso import CursoResumo

if TYPE_CHECKING:
    from app.domain.entities.aluno import AlunoResumo


@dataclass(frozen=True)
class DisciplinaResumo:
    id: int
    nome: str
    carga_horaria: int
    curso_id: int | None = None


@dataclass(frozen=True)
class MatriculaDaDisciplina:
    aluno_id: int
    disciplina_id: int
    aluno: Optional["AlunoResumo"] = None


@dataclass(frozen=True)
class Disciplina:
    id: int
    nome: str
    carga_horaria: int
    curso_id: int
    criado_em: datetime
    alterado_em: datetime
    curso: CursoResumo
    matricula: list[MatriculaDaDisciplina] = field(default_factory=list)
