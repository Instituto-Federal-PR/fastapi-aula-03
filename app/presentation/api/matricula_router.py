from fastapi import APIRouter, Depends, status

from app.application.dtos.matricula import MatriculaDTO
from app.application.use_cases.matricula import MatriculaUseCases
from app.presentation.dependencies import (
    get_matricula_use_cases, requer_coordenador, requer_professor_ou_coordenador,
)
from app.presentation.schemas.matricula_schemas import MatriculaCreate, MatriculaResponse

router = APIRouter(prefix="/matriculas", tags=["Matriculas"])


@router.post("", response_model=MatriculaResponse, status_code=status.HTTP_201_CREATED)
async def criar_matricula(
    dados: MatriculaCreate,
    use_cases: MatriculaUseCases = Depends(get_matricula_use_cases),
    _=Depends(requer_coordenador),
):
    return await use_cases.criar_matricula(MatriculaDTO(dados.aluno_id, dados.disciplina_id))


@router.get("", response_model=list[MatriculaResponse])
async def listar_matriculas(
    use_cases: MatriculaUseCases = Depends(get_matricula_use_cases),
    _=Depends(requer_professor_ou_coordenador),
):
    return await use_cases.listar_matriculas()


@router.get("/{aluno_id}/{disciplina_id}", response_model=MatriculaResponse)
async def buscar_matricula(
    aluno_id: int,
    disciplina_id: int,
    use_cases: MatriculaUseCases = Depends(get_matricula_use_cases),
    _=Depends(requer_professor_ou_coordenador),
):
    return await use_cases.buscar_matricula(aluno_id, disciplina_id)


@router.delete("/{aluno_id}/{disciplina_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_matricula(
    aluno_id: int,
    disciplina_id: int,
    use_cases: MatriculaUseCases = Depends(get_matricula_use_cases),
    _=Depends(requer_coordenador),
):
    await use_cases.deletar_matricula(aluno_id, disciplina_id)
    return None
