from app.application.dtos.matricula import MatriculaDTO
from app.core.exceptions import InvalidReference, NotFound
from app.domain.entities.matricula import Matricula
from app.domain.repositories.aluno_repository import AlunoRepository
from app.domain.repositories.disciplina_repository import DisciplinaRepository
from app.domain.repositories.matricula_repository import MatriculaRepository


class MatriculaUseCases:
    def __init__(
        self,
        repository: MatriculaRepository,
        aluno_repository: AlunoRepository,
        disciplina_repository: DisciplinaRepository,
    ):
        self.repository = repository
        self.alunos = aluno_repository
        self.disciplinas = disciplina_repository

    async def criar_matricula(self, dados: MatriculaDTO) -> Matricula:
        if await self.alunos.get_aluno(dados.aluno_id) is None:
            raise InvalidReference(
                f"Não é possível efetuar a matrícula. O aluno com ID {dados.aluno_id} não existe."
            )
        if await self.disciplinas.get_disciplina(dados.disciplina_id) is None:
            raise InvalidReference(
                f"Não é possível efetuar a matrícula. A disciplina com ID {dados.disciplina_id} não existe."
            )
        return await self.repository.create_matricula(dados.aluno_id, dados.disciplina_id)

    async def listar_matriculas(self) -> list[Matricula]:
        return await self.repository.list_matriculas()

    async def buscar_matricula(self, aluno_id: int, disciplina_id: int) -> Matricula:
        matricula = await self.repository.get_matricula(aluno_id, disciplina_id)
        if matricula is None:
            raise NotFound("Matrícula não encontrada!")
        return matricula

    async def deletar_matricula(self, aluno_id: int, disciplina_id: int) -> None:
        if not await self.repository.delete_matricula(aluno_id, disciplina_id):
            raise NotFound("Matrícula não encontrada")
