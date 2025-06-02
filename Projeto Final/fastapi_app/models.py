from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_app.database import Base

class Curso(Base):
    __tablename__ = "meu_app_curso"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)

class Aluno(Base):
    __tablename__ = "meu_app_aluno"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True)

class Matricula(Base):
    __tablename__ = "meu_app_matricula"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("meu_app_aluno.id"))
    curso_id = Column(Integer, ForeignKey("meu_app_curso.id"))
