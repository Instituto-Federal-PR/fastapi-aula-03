from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DisciplinaResumoSchema(BaseModel):
    id: int
    nome: str
    carga_horaria: int
    model_config = ConfigDict(from_attributes=True)


class CursoResumoSchema(BaseModel):
    id: int
    nome: str
    duracao: int
    model_config = ConfigDict(from_attributes=True)


class CursoCreate(BaseModel):
    nome: str
    duracao: int


class CursoResponse(BaseModel):
    id: int
    nome: str
    duracao: int
    criado_em: datetime
    alterado_em: datetime
    disciplina: list[DisciplinaResumoSchema] = []
    model_config = ConfigDict(from_attributes=True)
