from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_app import crud, schemas
from fastapi_app.database import SessionLocal

router = APIRouter()

# Dependência de sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/cursos/", response_model=list[schemas.Curso])
def listar_cursos(db: Session = Depends(get_db)):
    return crud.get_cursos(db)

@router.post("/cursos/", response_model=schemas.Curso)
def criar_curso(curso: schemas.CursoCreate, db: Session = Depends(get_db)):
    return crud.create_curso(db, curso)
