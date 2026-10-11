from app.application.dtos.curso import CursoDTO
from app.core.exceptions import NotFound
from app.domain.repositories.curso_repository import CursoRepository
from app.domain.entities.curso import Curso


class CursoUseCases:
    def __init__(self, repository: CursoRepository):
        self.repository = repository

    async def criar_curso(self, dados: CursoDTO) -> Curso:
        return await self.repository.create_curso(dados.nome, dados.duracao)

    async def listar_cursos(self) -> list[Curso]:
        return await self.repository.list_cursos()

    async def buscar_curso(self, curso_id: int) -> Curso:
        curso = await self.repository.get_curso(curso_id)
        if curso is None:
            raise NotFound("Curso não encontrado")
        return curso

    async def atualizar_curso(self, curso_id: int, dados: CursoDTO) -> Curso:
        curso = await self.repository.update_curso(curso_id, dados.nome, dados.duracao)
        if curso is None:
            raise NotFound("Curso não encontrado")
        return curso

    async def deletar_curso(self, curso_id: int) -> None:
        if not await self.repository.delete_curso(curso_id):
            raise NotFound("Curso não encontrado")
