

from datetime import datetime

from django.shortcuts import render

from blog.models import Posteo

def inicio(request):
    posteos = Posteo.objects.all().order_by('-fecha_publicacion')
    
    http_response = render (
        request=request,
        template_name="inicio.html",
        context = { "posteos" : posteos
                    }    
    )
    return http_response