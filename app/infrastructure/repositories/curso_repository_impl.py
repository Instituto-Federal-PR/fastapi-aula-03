from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.domain.entities.curso import Curso
from app.domain.repositories.curso_repository import CursoRepository
from app.infrastructure.database.models import CursoModel
from app.infrastructure.repositories._mappers import map_curso


class CursoRepositoryImpl(CursoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    @staticmethod
    def _statement():
        return select(CursoModel).options(selectinload(CursoModel.disciplina))

    async def create_curso(self, nome: str, duracao: int) -> Curso:
        row = CursoModel(nome=nome, duracao=duracao)
        self.session.add(row)
        await self.session.commit()
        result = await self.get_curso(row.id)
        assert result is not None
        return result

    async def list_cursos(self) -> list[Curso]:
        rows = (await self.session.scalars(self._statement())).all()
        return [map_curso(row) for row in rows]

    async def get_curso(self, curso_id: int) -> Curso | None:
        row = await self.session.scalar(self._statement().where(CursoModel.id == curso_id))
        return map_curso(row) if row else None

    async def update_curso(self, curso_id: int, nome: str, duracao: int) -> Curso | None:
        row = await self.session.get(CursoModel, curso_id)
        if row is None:
            return None
        row.nome, row.duracao = nome, duracao
        await self.session.commit()
        return await self.get_curso(curso_id)

    async def delete_curso(self, curso_id: int) -> bool:
        row = await self.session.get(CursoModel, curso_id)
        if row is None:
            return False
        await self.session.delete(row)
        await self.session.commit()
        return True
