from django.urls import path
from . import views
from .views import index, process_image


urlpatterns = [
    path('', index, name='index'),
    path('process_image/', process_image, name='process_image'),
]


