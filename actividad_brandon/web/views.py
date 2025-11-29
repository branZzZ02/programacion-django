from django.shortcuts import render
from django.http import HttpResponse

# ruta pruebas con un mensaje
def vista_pruebas(request):
    return HttpResponse("<h1>Bienvenido a Django desde unitecnar  actividad 1 </h1>")

# Ruta de template que muestra un div.
def vista_template(request):
    return render(request, 'index.html')


