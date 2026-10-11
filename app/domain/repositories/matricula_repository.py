from abc import ABC, abstractmethod

from app.domain.entities.matricula import Matricula


class MatriculaRepository(ABC):
    @abstractmethod
    async def create_matricula(self, aluno_id: int, disciplina_id: int) -> Matricula: ...

    @abstractmethod
    async def list_matriculas(self) -> list[Matricula]: ...

    @abstractmethod
    async def get_matricula(self, aluno_id: int, disciplina_id: int) -> Matricula | None: ...

    @abstractmethod
    async def delete_matricula(self, aluno_id: int, disciplina_id: int) -> bool: ...
