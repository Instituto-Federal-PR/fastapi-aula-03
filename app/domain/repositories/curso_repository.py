from abc import ABC, abstractmethod

from app.domain.entities.curso import Curso


class CursoRepository(ABC):
    @abstractmethod
    async def create_curso(self, nome: str, duracao: int) -> Curso: ...

    @abstractmethod
    async def list_cursos(self) -> list[Curso]: ...

    @abstractmethod
    async def get_curso(self, curso_id: int) -> Curso | None: ...

    @abstractmethod
    async def update_curso(self, curso_id: int, nome: str, duracao: int) -> Curso | None: ...

    @abstractmethod
    async def delete_curso(self, curso_id: int) -> bool: ...
