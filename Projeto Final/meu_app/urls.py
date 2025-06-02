from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import (
    CursoViewSet,
    AlunoViewSet,
    MatriculaViewSet,
    InstrutorViewSet,
    CategoriaViewSet,
    AulaViewSet,
)

# Rotas Tradicional do Projeto
urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('curso/<int:curso_id>/', views.detalhar_curso, name='detalhar_curso'),
    path('curso/<int:curso_id>/matricular/', views.matricular, name='matricular'),
    path('matricula/', views.matricular_geral, name='matricula_geral'),
    path('alunos/', views.listar_alunos, name='listar_alunos'),

    # FBV
    path('fbv/cursos/novo/', views.criar_curso, name='curso_criar_fbv'),
    path('fbv/cursos/<int:pk>/editar/', views.editar_curso, name='curso_editar_fbv'),
    path('fbv/cursos/<int:pk>/', views.detalhar_curso_funcao, name='curso_detalhar_fbv'),
    path('fbv/cursos/listar/', views.listar_cursos_funcao, name='curso_listar_fbv'),
    path('fbv/cursos/<int:pk>/deletar/', views.deletar_curso, name='curso_deletar_fbv'),

    # CBV
    path('cbv/cursos/novo/', views.CursoCreateView.as_view(), name='curso_criar_cbv'),
    path('cbv/cursos/<int:pk>/editar/', views.CursoUpdateView.as_view(), name='curso_editar_cbv'),
    path('cbv/cursos/<int:pk>/', views.CursoDetailView.as_view(), name='curso_detalhar_cbv'),
    path('cbv/cursos/listar/', views.CursoListView.as_view(), name='curso_listar_cbv'),
    path('cbv/cursos/<int:pk>/deletar/', views.CursoDeleteView.as_view(), name='curso_deletar_cbv'),
]

# ROTAS DA API DRF
router = DefaultRouter()
router.register(r'api/cursos', CursoViewSet)
router.register(r'api/alunos', AlunoViewSet)
router.register(r'api/matriculas', MatriculaViewSet)
router.register(r'api/instrutores', InstrutorViewSet)
router.register(r'api/categorias', CategoriaViewSet)
router.register(r'api/aulas', AulaViewSet)

urlpatterns += router.urls 