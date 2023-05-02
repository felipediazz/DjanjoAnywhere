from django.shortcuts import render
import requests
from .forms import ImageUploadForm

from django.conf import settings
from django.core.files.storage import FileSystemStorage

import pandas as pd
import numpy as np
import cv2
import os

from nbconvert import PythonExporter
import nbformat

# Create your views here.

##def home(request):

##    return render(request, 'core/home.html')

def index(request):
    form = ImageUploadForm()
    return render(request, 'core/index.html', {'form': form})


def process_image(request):
    if request.method == 'POST' and request.FILES['image']:
        # SE GUARDA LA IMAGEN
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        # SE CARGA LA IMAGEN EN UN ARREGLO NUMPY
        image_path = os.path.join(settings.MEDIA_ROOT, filename)
        image = cv2.imread(image_path)

        # SE PROCESA LA IMAGEN CON EL NOTEBOOK JUPYTER
        result_path = os.path.join(settings.MEDIA_ROOT, 'result.csv')
        with open('Sam.ipynb') as f:
            nb = nbformat.read(f, as_version=4)
            exporter = PythonExporter()
            source, _ = exporter.from_notebook_node(nb)

        exec(source)
        result_df = process_image(image)

        result_df.to_csv(result_path, index=False)

        # SE ELIMINA LAS IMAGENES ALMACENADAS
        os.remove(image_path)
        os.remove(result_path)

        # SE MUESTRA LA IMAGEN
        return render(request, 'core/result.html', {'result': result_df})

    #     result_path = os.path.join(settings.MEDIA_ROOT, 'result.csv')
    #     result_df = pd.read_csv(result_path)

    #     os.remove(image_path)
    #     os.remove(result_path)

    #     return render(request, 'result.html', {'result': result_df})

    else:
        form = ImageUploadForm()
        return render(request, 'core/index.html', {'form': form})