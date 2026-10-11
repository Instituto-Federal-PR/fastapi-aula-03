from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AlunoDaMatriculaSchema(BaseModel):
    id: int
    nome: str
    turma: int
    curso_id: int
    model_config = ConfigDict(from_attributes=True)


class DisciplinaDaMatriculaSchema(BaseModel):
    id: int
    nome: str
    carga_horaria: int
    curso_id: int
    model_config = ConfigDict(from_attributes=True)


class MatriculaCreate(BaseModel):
    aluno_id: int
    disciplina_id: int


class MatriculaResponse(BaseModel):
    aluno_id: int
    disciplina_id: int
    criado_em: datetime
    aluno: AlunoDaMatriculaSchema
    disciplina: DisciplinaDaMatriculaSchema
    model_config = ConfigDict(from_attributes=True)
