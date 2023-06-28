from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente
from .models import Requerimiento
from .models import RequerimientoEspecif
from .forms import ClienteAddForm
from .forms import RequerimientoAddForm
from .forms import RequerimientoEspecifAddForm

def index(request):
    return render(request, "index.html")

def error_404(request, exception):
    return render(request, '403.html', status=404)

def requerimiento(request):
    requerimientos = Requerimiento.objects.all()
    return render(request,"requerimientos.html",{'requerimientos':requerimientos})
    
def requerimientoEspecif(request):
    requerimientosEspecif = RequerimientoEspecif.objects.all()
    return render(request,"requerimientosEspecif.html",{'requerimientosEspecif':requerimientosEspecif})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request,"clientes.html",{'clientes':clientes})

def add_cliente(request):
    form = ClienteAddForm (request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_cliente = form.save()
            messages.success(request, "Cliente añadido")
            return redirect('index')
    return render(request,'add_cliente.html',{'form':form})

def add_requerimiento(request):
    form = RequerimientoAddForm (request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_requerimiento = form.save()
            messages.success(request, "Requerimiento añadido")
            return redirect('index')
    return render(request,'add_requerimiento.html',{'form':form})
    
def add_requerimientoEspecif(request):
    form = RequerimientoEspecifAddForm (request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_requerimientoEspecif = form.save()
            messages.success(request, "Requerimiento Especifico añadido")
            return redirect('index')
    return render(request,'add_requerimientoEspecif.html',{'form':form})
    