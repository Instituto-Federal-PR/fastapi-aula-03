from dataclasses import dataclass


@dataclass(frozen=True)
class CursoDTO:
    nome: str
    duracao: int
