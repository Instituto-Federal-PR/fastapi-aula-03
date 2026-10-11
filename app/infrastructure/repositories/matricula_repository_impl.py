from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.domain.entities.matricula import Matricula
from app.domain.repositories.matricula_repository import MatriculaRepository
from app.infrastructure.database.models import AlunoModel, DisciplinaModel, MatriculaModel
from app.infrastructure.repositories._mappers import map_matricula


class MatriculaRepositoryImpl(MatriculaRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    @staticmethod
    def _statement():
        return select(MatriculaModel).options(
            selectinload(MatriculaModel.aluno),
            selectinload(MatriculaModel.disciplina),
        )

    async def create_matricula(self, aluno_id: int, disciplina_id: int) -> Matricula:
        row = MatriculaModel(aluno_id=aluno_id, disciplina_id=disciplina_id)
        self.session.add(row)
        await self.session.commit()
        result = await self.get_matricula(aluno_id, disciplina_id)
        assert result is not None
        return result

    async def list_matriculas(self) -> list[Matricula]:
        rows = (await self.session.scalars(self._statement())).all()
        return [map_matricula(row) for row in rows]

    async def get_matricula(self, aluno_id: int, disciplina_id: int) -> Matricula | None:
        row = await self.session.scalar(
            self._statement().where(
                MatriculaModel.aluno_id == aluno_id,
                MatriculaModel.disciplina_id == disciplina_id,
            )
        )
        return map_matricula(row) if row else None

    async def delete_matricula(self, aluno_id: int, disciplina_id: int) -> bool:
        row = await self.session.get(MatriculaModel, (aluno_id, disciplina_id))
        if row is None:
            return False
        await self.session.delete(row)
        await self.session.commit()
        return True
