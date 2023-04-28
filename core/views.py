from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def obtener_imagen(request):
    with open('/ruta/a/la/imagen.jpg', 'rb') as f:
        imagen_data = f.read()
    return HttpResponse(imagen_data, content_type="image/jpeg")