from fastapi import APIRouter, Depends, status

from app.application.dtos.disciplina import DisciplinaDTO
from app.application.use_cases.disciplina import DisciplinaUseCases
from app.presentation.dependencies import (
    get_disciplina_use_cases, requer_professor, requer_professor_ou_coordenador,
)
from app.presentation.schemas.disciplina_schemas import DisciplinaCreate, DisciplinaResponse

router = APIRouter(prefix="/disciplinas", tags=["Disciplinas"])


@router.post("", response_model=DisciplinaResponse, status_code=status.HTTP_201_CREATED)
async def criar_disciplina(
    dados: DisciplinaCreate,
    use_cases: DisciplinaUseCases = Depends(get_disciplina_use_cases),
    _=Depends(requer_professor),
):
    return await use_cases.criar_disciplina(
        DisciplinaDTO(dados.nome, dados.carga_horaria, dados.curso_id)
    )


@router.get("", response_model=list[DisciplinaResponse])
async def listar_disciplinas(
    use_cases: DisciplinaUseCases = Depends(get_disciplina_use_cases),
    _=Depends(requer_professor_ou_coordenador),
):
    return await use_cases.listar_disciplinas()


@router.get("/{disciplina_id}", response_model=DisciplinaResponse)
async def buscar_disciplina(
    disciplina_id: int,
    use_cases: DisciplinaUseCases = Depends(get_disciplina_use_cases),
    _=Depends(requer_professor_ou_coordenador),
):
    return await use_cases.buscar_disciplina(disciplina_id)


@router.put("/{disciplina_id}", response_model=DisciplinaResponse)
async def atualizar_disciplina(
    disciplina_id: int,
    dados: DisciplinaCreate,
    use_cases: DisciplinaUseCases = Depends(get_disciplina_use_cases),
    _=Depends(requer_professor),
):
    return await use_cases.atualizar_disciplina(
        disciplina_id, DisciplinaDTO(dados.nome, dados.carga_horaria, dados.curso_id)
    )


@router.delete("/{disciplina_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_disciplina(
    disciplina_id: int,
    use_cases: DisciplinaUseCases = Depends(get_disciplina_use_cases),
    _=Depends(requer_professor),
):
    await use_cases.deletar_disciplina(disciplina_id)
    return None
