from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.domain.entities.aluno import Aluno
from app.domain.repositories.aluno_repository import AlunoRepository
from app.infrastructure.database.models import AlunoModel, MatriculaModel
from app.infrastructure.repositories._mappers import map_aluno


class AlunoRepositoryImpl(AlunoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    @staticmethod
    def _statement():
        return select(AlunoModel).options(
            selectinload(AlunoModel.curso),
            selectinload(AlunoModel.matricula).selectinload(MatriculaModel.disciplina),
        )

    async def create_aluno(self, nome: str, turma: int, curso_id: int) -> Aluno:
        row = AlunoModel(nome=nome, turma=turma, curso_id=curso_id)
        self.session.add(row)
        await self.session.commit()
        result = await self.get_aluno(row.id)
        assert result is not None
        return result

    async def list_alunos(self) -> list[Aluno]:
        rows = (await self.session.scalars(self._statement())).all()
        return [map_aluno(row) for row in rows]

    async def get_aluno(self, aluno_id: int) -> Aluno | None:
        row = await self.session.scalar(self._statement().where(AlunoModel.id == aluno_id))
        return map_aluno(row) if row else None

    async def update_aluno(
        self, aluno_id: int, nome: str, turma: int, curso_id: int
    ) -> Aluno | None:
        row = await self.session.get(AlunoModel, aluno_id)
        if row is None:
            return None
        row.nome, row.turma, row.curso_id = nome, turma, curso_id
        await self.session.commit()
        return await self.get_aluno(aluno_id)

    async def delete_aluno(self, aluno_id: int) -> bool:
        row = await self.session.get(AlunoModel, aluno_id)
        if row is None:
            return False
        await self.session.delete(row)
        await self.session.commit()
        return True
