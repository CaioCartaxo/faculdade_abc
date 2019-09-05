from django.urls import path
from .views import index, cadastro, cadastro_ok, entrar, entrar_erro, sair, entrar_ok, editar_perfil, editar_perfil_ok, cadastro_erro, criar_curso, criar_curso_ok, inscricao, inscricao_curso_ok, cursos_bacharel

urlpatterns = [
    path('', index, name='index'),
    path('inicio/', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastro_ok/', cadastro_ok, name='cadastro_ok'),
    path('cadastro_erro/', cadastro_erro, name='cadastro_erro'),
    path('entrar/', entrar, name='entrar'),
    path('entrar_erro/', entrar_erro, name='entrar_erro'),
    path('entrar_ok/', entrar_ok, name='entrar_ok'),
    path('sair/', sair, name='sair'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('editar_perfil_ok/', editar_perfil_ok, name='editar_perfil_ok'),
    path('criar_curso/', criar_curso, name='criar_curso'),
    path('criar_curso_ok/', criar_curso_ok, name='criar_curso_ok'),
    path('inscricao/', inscricao, name='inscricao'),
    path('inscricao_ok/', inscricao_curso_ok, name='inscricao_ok'),
    path('cursos_bacharel/', cursos_bacharel, name='cursos_bacharel'),
]
