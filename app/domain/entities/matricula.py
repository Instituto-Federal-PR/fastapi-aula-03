from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.entities.aluno import AlunoResumo
    from app.domain.entities.disciplina import DisciplinaResumo


@dataclass(frozen=True)
class Matricula:
    aluno_id: int
    disciplina_id: int
    criado_em: datetime
    aluno: "AlunoResumo"
    disciplina: "DisciplinaResumo"