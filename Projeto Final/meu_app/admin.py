from django.contrib import admin

from django.contrib import admin
from .models import Categoria, Instrutor, Curso, Aula, Aluno, Matricula, Progresso, Avaliacao

admin.site.register(Categoria)
admin.site.register(Instrutor)
admin.site.register(Curso)
admin.site.register(Aula)
admin.site.register(Aluno)
admin.site.register(Matricula)
admin.site.register(Progresso)
admin.site.register(Avaliacao)
