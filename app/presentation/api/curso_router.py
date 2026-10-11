from fastapi import APIRouter, Depends, status

from app.application.dtos.curso import CursoDTO
from app.application.use_cases.curso import CursoUseCases
from app.presentation.dependencies import (
    get_curso_use_cases, requer_coordenador, requer_professor_ou_coordenador,
)
from app.presentation.schemas.curso_schemas import CursoCreate, CursoResponse

router = APIRouter(prefix="/cursos", tags=["Cursos"])


@router.post("", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
async def criar_curso(
    dados: CursoCreate,
    use_cases: CursoUseCases = Depends(get_curso_use_cases),
    _=Depends(requer_coordenador),
):
    return await use_cases.criar_curso(CursoDTO(dados.nome, dados.duracao))


@router.get("", response_model=list[CursoResponse])
async def listar_cursos(
    use_cases: CursoUseCases = Depends(get_curso_use_cases),
    _=Depends(requer_professor_ou_coordenador),
):
    return await use_cases.listar_cursos()


@router.get("/{curso_id}", response_model=CursoResponse)
async def buscar_curso(
    curso_id: int,
    use_cases: CursoUseCases = Depends(get_curso_use_cases),
    _=Depends(requer_professor_ou_coordenador),
):
    return await use_cases.buscar_curso(curso_id)


@router.put("/{curso_id}", response_model=CursoResponse)
async def atualizar_curso(
    curso_id: int,
    dados: CursoCreate,
    use_cases: CursoUseCases = Depends(get_curso_use_cases),
    _=Depends(requer_coordenador),
):
    return await use_cases.atualizar_curso(curso_id, CursoDTO(dados.nome, dados.duracao))


@router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_curso(
    curso_id: int,
    use_cases: CursoUseCases = Depends(get_curso_use_cases),
    _=Depends(requer_coordenador),
):
    await use_cases.deletar_curso(curso_id)
    return None
