"""Adiciona as tabelas de aluno e matrícula que faltavam na migração inicial.

Revision ID: b813b924ce11
Revises: 4a7aa759f7d1
Create Date: 2026-10-05
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "b813b924ce11"
down_revision: Union[str, Sequence[str], None] = "4a7aa759f7d1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "alunos",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("turma", sa.Integer(), nullable=False),
        sa.Column("curso_id", sa.Integer(), nullable=False),
        sa.Column("criado_em", sa.DateTime(), nullable=True),
        sa.Column("alterado_em", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["curso_id"], ["cursos.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_alunos_id"), "alunos", ["id"], unique=False)
    op.create_table(
        "matriculas",
        sa.Column("aluno_id", sa.Integer(), nullable=False),
        sa.Column("disciplina_id", sa.Integer(), nullable=False),
        sa.Column("criado_em", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["aluno_id"], ["alunos.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["disciplina_id"], ["disciplinas.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("aluno_id", "disciplina_id"),
    )


def downgrade() -> None:
    op.drop_table("matriculas")
    op.drop_index(op.f("ix_alunos_id"), table_name="alunos")
    op.drop_table("alunos")
