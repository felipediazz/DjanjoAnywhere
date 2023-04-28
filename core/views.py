from django.shortcuts import render
import requests


# Create your views here.

##def home(request):

##    return render(request, 'core/home.html')

def home(request):
    if request.method == 'POST' and request.FILES['imagen']:
        imagen = request.FILES['imagen'].read()
        url = 'http://localhost:8888/upload'
        files = {'imagen': imagen}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            imagen_variable = response.json()['imagen']
            # Haz algo con la variable de imagen aquí
    return render(request, 'core/home.html')