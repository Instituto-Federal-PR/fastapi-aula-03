from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.presentation.schemas.curso_schemas import CursoResumoSchema


class AlunoResumoSchema(BaseModel):
    id: int
    nome: str
    turma: int
    model_config = ConfigDict(from_attributes=True)


class MatriculaDaDisciplinaSchema(BaseModel):
    aluno_id: int
    disciplina_id: int
    aluno: Optional[AlunoResumoSchema] = None
    model_config = ConfigDict(from_attributes=True)


class DisciplinaCreate(BaseModel):
    nome: str
    carga_horaria: int
    curso_id: int


class DisciplinaResponse(BaseModel):
    id: int
    nome: str
    carga_horaria: int
    curso_id: int
    criado_em: datetime
    alterado_em: datetime
    curso: CursoResumoSchema
    matricula: list[MatriculaDaDisciplinaSchema] = []
    model_config = ConfigDict(from_attributes=True)
