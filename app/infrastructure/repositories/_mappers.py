from app.domain.entities.aluno import Aluno, AlunoResumo, MatriculaDoAluno
from app.domain.entities.curso import Curso, CursoResumo
from app.domain.entities.disciplina import (
    Disciplina, DisciplinaResumo, MatriculaDaDisciplina,
)
from app.domain.entities.matricula import Matricula
from app.infrastructure.database.models import (
    AlunoModel, CursoModel, DisciplinaModel, MatriculaModel,
)


def curso_resumo(row: CursoModel) -> CursoResumo:
    return CursoResumo(row.id, row.nome, row.duracao)


def disciplina_resumo(row: DisciplinaModel) -> DisciplinaResumo:
    return DisciplinaResumo(row.id, row.nome, row.carga_horaria, row.curso_id)


def aluno_resumo(row: AlunoModel) -> AlunoResumo:
    return AlunoResumo(row.id, row.nome, row.turma, row.curso_id)


def map_curso(row: CursoModel) -> Curso:
    return Curso(
        id=row.id,
        nome=row.nome,
        duracao=row.duracao,
        criado_em=row.criado_em,
        alterado_em=row.alterado_em,
        disciplina=[disciplina_resumo(item) for item in row.disciplina],
    )


def map_aluno(row: AlunoModel) -> Aluno:
    return Aluno(
        id=row.id,
        nome=row.nome,
        turma=row.turma,
        curso_id=row.curso_id,
        criado_em=row.criado_em,
        alterado_em=row.alterado_em,
        curso=curso_resumo(row.curso),
        matricula=[
            MatriculaDoAluno(
                aluno_id=item.aluno_id,
                disciplina_id=item.disciplina_id,
                disciplina=disciplina_resumo(item.disciplina),
            )
            for item in row.matricula
        ],
    )


def map_disciplina(row: DisciplinaModel) -> Disciplina:
    return Disciplina(
        id=row.id,
        nome=row.nome,
        carga_horaria=row.carga_horaria,
        curso_id=row.curso_id,
        criado_em=row.criado_em,
        alterado_em=row.alterado_em,
        curso=curso_resumo(row.curso),
        matricula=[
            MatriculaDaDisciplina(
                aluno_id=item.aluno_id,
                disciplina_id=item.disciplina_id,
                aluno=aluno_resumo(item.aluno),
            )
            for item in row.matricula
        ],
    )


def map_matricula(row: MatriculaModel) -> Matricula:
    return Matricula(
        aluno_id=row.aluno_id,
        disciplina_id=row.disciplina_id,
        criado_em=row.criado_em,
        aluno=aluno_resumo(row.aluno),
        disciplina=disciplina_resumo(row.disciplina),
    )
