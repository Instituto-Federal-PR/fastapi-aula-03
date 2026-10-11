from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.entities.disciplina import DisciplinaResumo


@dataclass(frozen=True)
class CursoResumo:
    id: int
    nome: str
    duracao: int


@dataclass(frozen=True)
class Curso:
    id: int
    nome: str
    duracao: int
    criado_em: datetime
    alterado_em: datetime
    disciplina: list["DisciplinaResumo"] = field(default_factory=list)
