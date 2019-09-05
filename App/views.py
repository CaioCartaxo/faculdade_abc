from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Cursos_Bacharel, Inscrito_Curso_Bacharel

def index(request, template_name='index.html'):

    return render(request, template_name)

def cadastro(request, template_name='cadastro.html'):
    if request.method == "POST":
        username = request.POST['username']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        if senha1 != senha2:
            return HttpResponseRedirect('/cadastro_erro/')
        else:
            user = User.objects.create_user(username, email, senha1)
            user.first_name = nome
            user.last_name = sobrenome
            user.save()
        return HttpResponseRedirect('/cadastro_ok/')

    return render(request, template_name)

def cadastro_erro(request, template_name='cadastro_erro.html'):

    return render(request, template_name)

def cadastro_ok(request, template_name='cadastro_ok.html'):

    return render(request, template_name)

def entrar(request, template_name='entrar.html'):
    next = request.GET.get('next', '/entrar_ok/')
    if request.method == "POST":
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(username=username, password=senha)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect('/entrar_erro/')

    return render(request, template_name)

@login_required
def entrar_ok(request, template_name='entrar_ok.html'):

    return render(request, template_name)

def entrar_erro(request, template_name='entrar_erro.html'):

    return render(request, template_name)

def sair(request):
    logout(request)
    return HttpResponseRedirect('/inicio/')

@login_required
def editar_perfil(request, template_name='editar_perfil.html'):
    user = request.user
    if request.method == "POST":
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        nascimento = request.POST['nascimento']
        profissao = request.POST['profissao']
        email = request.POST['email']
        endereco = request.POST['endereco']
        n_endereco = request.POST['n_endereco']
        bairro = request.POST['bairro']
        CEP = request.POST['CEP']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        telefone = request.POST['telefone']
        celular = request.POST['celular']
        user.first_name = nome
        user.last_name = sobrenome
        user.profile.nascimento = nascimento
        user.profile.profissao = profissao
        user.email = email
        user.profile.endereco = endereco
        user.profile.n_endereco = n_endereco
        user.profile.bairro = bairro
        user.profile.cep = CEP
        user.profile.cidade = cidade
        user.profile.estado = estado
        user.profile.telefone = telefone
        user.profile.celular = celular
        user.save()
        return HttpResponseRedirect('/editar_perfil_ok/')


    return render(request, template_name)

@login_required
def editar_perfil_ok(request, template_name='editar_perfil_ok.html'):

    return render(request, template_name)

@login_required
def criar_curso(request, template_name='criar_curso.html'):
    if request.method == "POST":
        n_curso = request.POST['n_curso']
        data_curso = request.POST['data_curso']
        periodos_curso = request.POST['periodos_curso']
        valor_curso = request.POST['valor_curso']

        Cursos_Bacharel.objects.create(
            n_curso=n_curso,
            data_curso=data_curso,
            periodos_curso=periodos_curso,
            valor_curso=valor_curso
        )
        return HttpResponseRedirect('/criar_curso_ok/')

    return render(request, template_name)

@login_required
def criar_curso_ok(request, template_name='criar_curso_ok.html'):

    return render(request, template_name)

@login_required
def inscricao(request, template_name='inscricao_curso.html'):
    user = request.user
    #usuario = User.objects.get(user)
    #Cursos_Graduacao.objects.filter()
    if request.method == "POST":
        n_curso = request.POST['n_curso']

        Inscrito_Curso_Bacharel.objects.create(
            curso_inscrito=n_curso,
            aluno = user
        )
        return HttpResponseRedirect('/inscricao_curso_ok/')

    return render(request, template_name)

@login_required
def inscricao_curso_ok(request, template_name='inscricao_curso_ok.html'):

    return render(request, template_name)

def cursos_bacharel(request, template_name='cursos_bacharel.html'):
    cursos = Cursos_Bacharel.objects.all()
    return render(request, template_name)