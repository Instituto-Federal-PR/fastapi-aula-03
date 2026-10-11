from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.presentation.schemas.curso_schemas import CursoResumoSchema


class DisciplinaDoAlunoSchema(BaseModel):
    id: int
    nome: str
    model_config = ConfigDict(from_attributes=True)


class MatriculaDoAlunoSchema(BaseModel):
    aluno_id: int
    disciplina_id: int
    disciplina: Optional[DisciplinaDoAlunoSchema] = None
    model_config = ConfigDict(from_attributes=True)


class AlunoCreate(BaseModel):
    nome: str
    turma: int
    curso_id: int


class AlunoResponse(BaseModel):
    id: int
    nome: str
    turma: int
    curso_id: int
    criado_em: datetime
    alterado_em: datetime
    curso: CursoResumoSchema
    matricula: list[MatriculaDoAlunoSchema] = []
    model_config = ConfigDict(from_attributes=True)
