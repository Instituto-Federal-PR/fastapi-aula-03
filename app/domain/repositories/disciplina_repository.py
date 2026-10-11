from abc import ABC, abstractmethod

from app.domain.entities.disciplina import Disciplina


class DisciplinaRepository(ABC):
    @abstractmethod
    async def create_disciplina(self, nome: str, carga_horaria: int, curso_id: int) -> Disciplina: ...

    @abstractmethod
    async def list_disciplinas(self) -> list[Disciplina]: ...

    @abstractmethod
    async def get_disciplina(self, disciplina_id: int) -> Disciplina | None: ...

    @abstractmethod
    async def update_disciplina(
        self, disciplina_id: int, nome: str, carga_horaria: int, curso_id: int
    ) -> Disciplina | None: ...

    @abstractmethod
    async def delete_disciplina(self, disciplina_id: int) -> bool: ...
