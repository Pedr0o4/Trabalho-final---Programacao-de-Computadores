"""
🧪 Testes dos Modelos com Templates

Este arquivo contém testes automatizados apenas para os modelos que possuem interação via templates
no sistema acadêmico: Curso, Aluno e Matrícula.
"""

from django.test import TestCase
from .models import Curso, Instrutor, Categoria, Aluno, Matricula
from datetime import date

class ModelosComTemplateTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Lógica", descricao="Cursos lógicos")
        self.instrutor = Instrutor.objects.create(nome="Carlos", bio="Professor de lógica", especializacao="Matemática")
        self.curso = Curso.objects.create(
            titulo="Curso de Lógica",
            descricao="Curso para iniciantes",
            instrutor=self.instrutor,
            categoria=self.categoria
        )
        self.aluno = Aluno.objects.create(
            nome="Maria Eduarda",
            email="maria@example.com",
            data_nascimento=date(2001, 5, 10)
        )

    def test_curso_template(self):
        self.assertEqual(self.curso.titulo, "Curso de Lógica")
        self.assertEqual(self.curso.instrutor.nome, "Carlos")

    def test_aluno_template(self):
        self.assertEqual(self.aluno.nome, "Maria Eduarda")

    def test_matricula_template(self):
        matricula = Matricula.objects.create(aluno=self.aluno, curso=self.curso)
        self.assertEqual(matricula.curso.titulo, "Curso de Lógica")
        self.assertEqual(matricula.aluno.email, "maria@example.com")
