from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.domain.entities.disciplina import Disciplina
from app.domain.repositories.disciplina_repository import DisciplinaRepository
from app.infrastructure.database.models import DisciplinaModel, MatriculaModel
from app.infrastructure.repositories._mappers import map_disciplina


class DisciplinaRepositoryImpl(DisciplinaRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    @staticmethod
    def _statement():
        return select(DisciplinaModel).options(
            selectinload(DisciplinaModel.curso),
            selectinload(DisciplinaModel.matricula).selectinload(MatriculaModel.aluno),
        )

    async def create_disciplina(
        self, nome: str, carga_horaria: int, curso_id: int
    ) -> Disciplina:
        row = DisciplinaModel(nome=nome, carga_horaria=carga_horaria, curso_id=curso_id)
        self.session.add(row)
        await self.session.commit()
        result = await self.get_disciplina(row.id)
        assert result is not None
        return result

    async def list_disciplinas(self) -> list[Disciplina]:
        rows = (await self.session.scalars(self._statement())).all()
        return [map_disciplina(row) for row in rows]

    async def get_disciplina(self, disciplina_id: int) -> Disciplina | None:
        row = await self.session.scalar(
            self._statement().where(DisciplinaModel.id == disciplina_id)
        )
        return map_disciplina(row) if row else None

    async def update_disciplina(
        self, disciplina_id: int, nome: str, carga_horaria: int, curso_id: int
    ) -> Disciplina | None:
        row = await self.session.get(DisciplinaModel, disciplina_id)
        if row is None:
            return None
        row.nome, row.carga_horaria, row.curso_id = nome, carga_horaria, curso_id
        await self.session.commit()
        return await self.get_disciplina(disciplina_id)

    async def delete_disciplina(self, disciplina_id: int) -> bool:
        row = await self.session.get(DisciplinaModel, disciplina_id)
        if row is None:
            return False
        await self.session.delete(row)
        await self.session.commit()
        return True
