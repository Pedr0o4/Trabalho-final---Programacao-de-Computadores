from sqlalchemy.orm import Session
from fastapi_app import models, schemas

# Curso 
def get_cursos(db: Session):
    return db.query(models.Curso).all()

def create_curso(db: Session, curso: schemas.CursoCreate):
    db_obj = models.Curso(**curso.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Aluno 
def get_alunos(db: Session):
    return db.query(models.Aluno).all()

def create_aluno(db: Session, aluno: schemas.AlunoCreate):
    db_obj = models.Aluno(**aluno.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Matricula 
def get_matriculas(db: Session):
    return db.query(models.Matricula).all()

def create_matricula(db: Session, matricula: schemas.MatriculaCreate):
    db_obj = models.Matricula(**matricula.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
    