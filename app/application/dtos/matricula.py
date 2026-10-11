from dataclasses import dataclass


@dataclass(frozen=True)
class MatriculaDTO:
    aluno_id: int
    disciplina_id: int
