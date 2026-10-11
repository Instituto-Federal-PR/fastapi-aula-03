from fastapi import APIRouter, Depends, status

from app.application.dtos.aluno import AlunoDTO
from app.application.use_cases.aluno import AlunoUseCases
from app.presentation.dependencies import (
    get_aluno_use_cases, requer_professor, requer_professor_ou_coordenador,
)
from app.presentation.schemas.aluno_schemas import AlunoCreate, AlunoResponse

router = APIRouter(prefix="/alunos", tags=["Alunos"])


@router.post("", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
async def criar_aluno(
    dados: AlunoCreate,
    use_cases: AlunoUseCases = Depends(get_aluno_use_cases),
    _=Depends(requer_professor),
):
    return await use_cases.criar_aluno(AlunoDTO(dados.nome, dados.turma, dados.curso_id))


@router.get("", response_model=list[AlunoResponse])
async def listar_alunos(
    use_cases: AlunoUseCases = Depends(get_aluno_use_cases),
    _=Depends(requer_professor_ou_coordenador),
):
    return await use_cases.listar_alunos()


@router.get("/{aluno_id}", response_model=AlunoResponse)
async def buscar_aluno(
    aluno_id: int,
    use_cases: AlunoUseCases = Depends(get_aluno_use_cases),
    _=Depends(requer_professor_ou_coordenador),
):
    return await use_cases.buscar_aluno(aluno_id)


@router.put("/{aluno_id}", response_model=AlunoResponse)
async def atualizar_aluno(
    aluno_id: int,
    dados: AlunoCreate,
    use_cases: AlunoUseCases = Depends(get_aluno_use_cases),
    _=Depends(requer_professor),
):
    return await use_cases.atualizar_aluno(
        aluno_id, AlunoDTO(dados.nome, dados.turma, dados.curso_id)
    )


@router.delete("/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_aluno(
    aluno_id: int,
    use_cases: AlunoUseCases = Depends(get_aluno_use_cases),
    _=Depends(requer_professor),
):
    await use_cases.deletar_aluno(aluno_id)
    return None
