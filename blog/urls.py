from django.contrib import admin
from django.urls import path, include

from blog.views import (PosteoListView, PosteoCreateView, PosteoDetailView, PosteoUpdateView,PosteoDeleteView, 
                        buscar_posteo)



urlpatterns = [
    path("posteos/", PosteoListView.as_view(), name="lista_posteos"),
    path('posteos/<int:pk>/', PosteoDetailView.as_view(), name="ver_posteo"),
    path('crear-posteo/', PosteoCreateView.as_view(), name="crear_posteo"),
    path('editar-posteo/<int:pk>/', PosteoUpdateView.as_view(), name="editar_posteo"),
    path('eliminar-posteo/<int:pk>/', PosteoDeleteView.as_view(), name="eliminar_posteo"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('buscar-posteo/', buscar_posteo, name= "buscar_posteo"),

]