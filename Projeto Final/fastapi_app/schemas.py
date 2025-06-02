from pydantic import BaseModel

# Curso
class CursoBase(BaseModel):
    titulo: str
    descricao: str

class CursoCreate(CursoBase):
    pass

class Curso(CursoBase):
    id: int

    class Config:
        orm_mode = True

# Aluno
class AlunoBase(BaseModel):
    nome: str
    email: str

class AlunoCreate(AlunoBase):
    pass

class Aluno(AlunoBase):
    id: int

    class Config:
        orm_mode = True

# Matricula
class MatriculaBase(BaseModel):
    aluno_id: int
    curso_id: int

class MatriculaCreate(MatriculaBase):
    pass

class Matricula(MatriculaBase):
    id: int

    class Config:
        orm_mode = True
