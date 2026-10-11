from dataclasses import dataclass


@dataclass(frozen=True)
class DisciplinaDTO:
    nome: str
    carga_horaria: int
    curso_id: int
