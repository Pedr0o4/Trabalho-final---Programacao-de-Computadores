from django.db import models

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Instrutor(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField()
    especializacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Aula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    video_url = models.URLField()
    duracao = models.IntegerField(help_text="Duração em minutos")

    def __str__(self):
        return f"{self.titulo} ({self.curso.titulo})"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.nome} em {self.curso.titulo}"

class Progresso(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('assistido', 'Assistido'), ('pendente', 'Pendente')])

    def __str__(self):
        return f"{self.aluno.nome} - {self.aula.titulo} ({self.status})"

class Avaliacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()

    def __str__(self):
        return f"{self.aluno.nome} avaliou {self.curso.titulo}"


