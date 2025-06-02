from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy

from .models import Curso, Aluno, Matricula, Instrutor, Categoria, Aula
from .forms import AlunoForm, MatriculaForm, CursoForm, AvaliacaoForm

# Página inicial
def home(request):
    contador = range(3)
    avaliacao_form = AvaliacaoForm()  

    if request.method == 'POST':
        avaliacao_form = AvaliacaoForm(request.POST)
        if avaliacao_form.is_valid():
            avaliacao_form.save()
            return redirect('home')

    return render(request, 'meu_app/home.html', {
        'contador': contador,
        'avaliacao_form': avaliacao_form
    })

# Lista de cursos 
def listar_cursos(request):
    cursos = Curso.objects.all()

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()

    return render(request, 'meu_app/cursos.html', {'cursos': cursos, 'form': form})

# Detalhes de um curso
def detalhar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'meu_app/curso_detalhe.html', {'curso': curso})

# Matrícula com curso pré-definido
def matricular(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = MatriculaForm(initial={'curso': curso})

    return render(request, 'meu_app/matricula_form.html', {'form': form, 'curso': curso})

# Matrícula geral com exibição das matrículas
def matricular_geral(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matricula_geral')  
    else:
        form = MatriculaForm()

    matriculas = Matricula.objects.all()  
    return render(request, 'meu_app/matricula_form.html', {'form': form, 'matriculas': matriculas})

# Lista e cadastro de alunos
def listar_alunos(request):
    alunos = Aluno.objects.all()

    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()

    return render(request, 'meu_app/alunos.html', {'alunos': alunos, 'form': form})

# FUNÇÕES FBV

def criar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'meu_app/curso_form.html', {'form': form})

def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'meu_app/curso_form.html', {'form': form})

def detalhar_curso_funcao(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'meu_app/curso_detalhe.html', {'curso': curso})

def listar_cursos_funcao(request):
    cursos = Curso.objects.all()
    return render(request, 'meu_app/cursos.html', {'cursos': cursos})

def deletar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, 'meu_app/curso_confirm_delete.html', {'curso': curso})

# CLASSES CBV

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'meu_app/curso_form.html'
    success_url = reverse_lazy('listar_cursos')

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'meu_app/curso_form.html'
    success_url = reverse_lazy('listar_cursos')

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'meu_app/curso_detalhe.html'

class CursoListView(ListView):
    model = Curso
    template_name = 'meu_app/cursos.html'
    context_object_name = 'cursos'

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'meu_app/curso_confirm_delete.html'
    success_url = reverse_lazy('listar_cursos')

# API Viewsets 

from rest_framework import viewsets
from .serializers import (
    CursoSerializer,
    AlunoSerializer,
    MatriculaSerializer,
    InstrutorSerializer,
    CategoriaSerializer,
    AulaSerializer,
)

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class InstrutorViewSet(viewsets.ModelViewSet):
    queryset = Instrutor.objects.all()
    serializer_class = InstrutorSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
