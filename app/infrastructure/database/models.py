import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.entities.user import UserRole
from app.infrastructure.database.session import Base


class CursoModel(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    duracao: Mapped[int] = mapped_column(Integer, nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    alterado_em: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    aluno: Mapped[list["AlunoModel"]] = relationship(
        back_populates="curso", cascade="all, delete-orphan"
    )
    disciplina: Mapped[list["DisciplinaModel"]] = relationship(
        back_populates="curso", cascade="all, delete-orphan"
    )


class AlunoModel(Base):
    __tablename__ = "alunos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    turma: Mapped[int] = mapped_column(Integer, nullable=False)
    curso_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("cursos.id", ondelete="CASCADE"), nullable=False
    )
    criado_em: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    alterado_em: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    curso: Mapped[CursoModel] = relationship(back_populates="aluno")
    matricula: Mapped[list["MatriculaModel"]] = relationship(back_populates="aluno")


class DisciplinaModel(Base):
    __tablename__ = "disciplinas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    carga_horaria: Mapped[int] = mapped_column(Integer, nullable=False)
    curso_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("cursos.id", ondelete="CASCADE"), nullable=False
    )
    criado_em: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    alterado_em: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    curso: Mapped[CursoModel] = relationship(back_populates="disciplina")
    matricula: Mapped[list["MatriculaModel"]] = relationship(back_populates="disciplina")


class MatriculaModel(Base):
    __tablename__ = "matriculas"

    aluno_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("alunos.id", ondelete="CASCADE"), primary_key=True
    )
    disciplina_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("disciplinas.id", ondelete="CASCADE"), primary_key=True
    )
    criado_em: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    aluno: Mapped[AlunoModel] = relationship(back_populates="matricula")
    disciplina: Mapped[DisciplinaModel] = relationship(back_populates="matricula")


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    role: Mapped[UserRole] = mapped_column(String(20), nullable=False, default=UserRole.PROFESSOR)
