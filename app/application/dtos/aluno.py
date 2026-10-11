from dataclasses import dataclass


@dataclass(frozen=True)
class AlunoDTO:
    nome: str
    turma: int
    curso_id: int
