from app.application.dtos.aluno import AlunoDTO
from app.core.exceptions import InvalidReference, NotFound
from app.domain.entities.aluno import Aluno
from app.domain.repositories.aluno_repository import AlunoRepository
from app.domain.repositories.curso_repository import CursoRepository


class AlunoUseCases:
    def __init__(self, repository: AlunoRepository, curso_repository: CursoRepository):
        self.repository = repository
        self.cursos = curso_repository

    async def criar_aluno(self, dados: AlunoDTO) -> Aluno:
        if await self.cursos.get_curso(dados.curso_id) is None:
            raise InvalidReference(
                f"Não é possível cadastrar o aluno. O curso com ID {dados.curso_id} não existe."
            )
        return await self.repository.create_aluno(dados.nome, dados.turma, dados.curso_id)

    async def listar_alunos(self) -> list[Aluno]:
        return await self.repository.list_alunos()

    async def buscar_aluno(self, aluno_id: int) -> Aluno:
        aluno = await self.repository.get_aluno(aluno_id)
        if aluno is None:
            raise NotFound("Aluno não encontrado")
        return aluno

    async def atualizar_aluno(self, aluno_id: int, dados: AlunoDTO) -> Aluno:
        if await self.repository.get_aluno(aluno_id) is None:
            raise NotFound("Aluno não encontrado")
        if await self.cursos.get_curso(dados.curso_id) is None:
            raise InvalidReference(f"Curso com ID {dados.curso_id} não existe.")
        aluno = await self.repository.update_aluno(
            aluno_id, dados.nome, dados.turma, dados.curso_id
        )
        if aluno is None:
            raise NotFound("Aluno não encontrado")
        return aluno

    async def deletar_aluno(self, aluno_id: int) -> None:
        if not await self.repository.delete_aluno(aluno_id):
            raise NotFound("Aluno não encontrado")
