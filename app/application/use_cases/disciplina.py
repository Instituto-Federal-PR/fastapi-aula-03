from app.application.dtos.disciplina import DisciplinaDTO
from app.core.exceptions import InvalidReference, NotFound
from app.domain.entities.disciplina import Disciplina
from app.domain.repositories.curso_repository import CursoRepository
from app.domain.repositories.disciplina_repository import DisciplinaRepository


class DisciplinaUseCases:
    def __init__(self, repository: DisciplinaRepository, curso_repository: CursoRepository):
        self.repository = repository
        self.cursos = curso_repository

    async def criar_disciplina(self, dados: DisciplinaDTO) -> Disciplina:
        if await self.cursos.get_curso(dados.curso_id) is None:
            raise InvalidReference(
                f"Não é possível criar a disciplina. O curso com ID {dados.curso_id} não existe."
            )
        return await self.repository.create_disciplina(
            dados.nome, dados.carga_horaria, dados.curso_id
        )

    async def listar_disciplinas(self) -> list[Disciplina]:
        return await self.repository.list_disciplinas()

    async def buscar_disciplina(self, disciplina_id: int) -> Disciplina:
        disciplina = await self.repository.get_disciplina(disciplina_id)
        if disciplina is None:
            raise NotFound("Disciplina não encontrada")
        return disciplina

    async def atualizar_disciplina(self, disciplina_id: int, dados: DisciplinaDTO) -> Disciplina:
        if await self.repository.get_disciplina(disciplina_id) is None:
            raise NotFound("Disciplina não encontrada")
        if await self.cursos.get_curso(dados.curso_id) is None:
            raise InvalidReference(f"Curso com ID {dados.curso_id} não existe.")
        disciplina = await self.repository.update_disciplina(
            disciplina_id, dados.nome, dados.carga_horaria, dados.curso_id
        )
        if disciplina is None:
            raise NotFound("Disciplina não encontrada")
        return disciplina

    async def deletar_disciplina(self, disciplina_id: int) -> None:
        if not await self.repository.delete_disciplina(disciplina_id):
            raise NotFound("Disciplina não encontrada")
