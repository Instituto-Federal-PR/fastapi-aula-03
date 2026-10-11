from abc import ABC, abstractmethod

from app.domain.entities.aluno import Aluno


class AlunoRepository(ABC):
    @abstractmethod
    async def create_aluno(self, nome: str, turma: int, curso_id: int) -> Aluno: ...

    @abstractmethod
    async def list_alunos(self) -> list[Aluno]: ...

    @abstractmethod
    async def get_aluno(self, aluno_id: int) -> Aluno | None: ...

    @abstractmethod
    async def update_aluno(self, aluno_id: int, nome: str, turma: int, curso_id: int) -> Aluno | None: ...

    @abstractmethod
    async def delete_aluno(self, aluno_id: int) -> bool: ...
