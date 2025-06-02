from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_app import crud, schemas
from fastapi_app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/matriculas/", response_model=list[schemas.Matricula])
def listar_matriculas(db: Session = Depends(get_db)):
    return crud.get_matriculas(db)

@router.post("/matriculas/", response_model=schemas.Matricula)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    return crud.create_matricula(db, matricula)
