from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form["nome_login"].value()
            senha=form["senha"].value()
        
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado com sucesso!")
            return redirect("index")
        else:
            messages.error(request, "Login ou senha incorretos.")
            return redirect("login")


    return render(request, "usuario/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

        if form.is_valid():
         
            nome=form["nome_cadastro"].value()
            email=form["email_cadastro"].value()
            senha=form["senha_cadastro"].value()

            if User.objects.filter(username=nome).exists():
                 messages.error(request, "Usuário existente!")
                 return redirect("cadastro")
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect("login")
    

    return render(request, "usuario/cadastro.html", {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout realizado com sucesso.")
    return redirect("login")
