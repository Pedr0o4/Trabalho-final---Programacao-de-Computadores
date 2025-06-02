from fastapi import FastAPI
from fastapi_app.routers import cursos, alunos, matriculas

app = FastAPI(
    title="API Acadêmica com FastAPI",
    version="1.0.0",
)

app.include_router(cursos.router)
app.include_router(alunos.router)
app.include_router(matriculas.router)
