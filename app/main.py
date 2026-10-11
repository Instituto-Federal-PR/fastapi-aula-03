from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import ApplicationError
from app.presentation.api.aluno_router import router as aluno_router
from app.presentation.api.auth_router import router as auth_router
from app.presentation.api.curso_router import router as curso_router
from app.presentation.api.disciplina_router import router as disciplina_router
from app.presentation.api.matricula_router import router as matricula_router

app = FastAPI(
    title="Sistema Acadêmico - Modular",
    description="API para gerenciamento de cursos e disciplinas",
    version="1.0.0",
)
app.include_router(auth_router)
app.include_router(aluno_router)
app.include_router(curso_router)
app.include_router(disciplina_router)
app.include_router(matricula_router)


@app.exception_handler(ApplicationError)
async def application_error_handler(request: Request, exc: ApplicationError):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à API do Sistema Acadêmico!"}
