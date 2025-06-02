from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_app import crud, schemas
from fastapi_app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db''
    finally:
        db.close()

@router.get("/alunos/", response_model=list[schemas.Aluno])
def listar_alunos(db: Session = Depends(get_db)):
    return crud.get_alunos(db)

@router.post("/alunos/", response_model=schemas.Aluno)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    return crud.create_aluno(db, aluno)
