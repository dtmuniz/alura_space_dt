from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url="login")
def index(request):
    fotografias = Fotografia.objects.order_by("data_publicacao").filter(publicada=True)
    return render(request, "galeria/index.html", {"cards": fotografias})
    
     
def imagem(request, foto_id):
    fotografia = get_object_or_404 (Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


@login_required(login_url="login")
def buscar(request):
    fotografias = Fotografia.objects.order_by("data_publicacao").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards": fotografias})

@login_required(login_url="login")
def nova_imagem(request):
    form = FotografiaForms
    if request.method == "POST" : 
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success (request, "Nova fotografia cadastrada")
            return redirect("index")
        
    return render(request, 'galeria/nova_imagem.html', {"form": form})

@login_required(login_url="login")
def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success (request, "Fotografia editada com sucesso!")
            return redirect("index")

    return render(request, "galeria/editar_imagem.html", {"form": form, "foto_id": foto_id})


@login_required(login_url="login")
def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, "A fotografia foi excluída com sucesso")
    
    return redirect ("index")


def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_publicacao").filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})