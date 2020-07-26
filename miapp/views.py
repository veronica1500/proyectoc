from django.shortcuts import render

# Create your views here.
def Inicio (request):
    return render(request,'inicio.html')
def Servicios (request):
    return render(request, 'servicios.html')
def Contactos (request):
    return render(request, 'contactos.html')

def Datos (request):
    return render(request, 'datos.html')