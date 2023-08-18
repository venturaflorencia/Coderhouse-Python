from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from perfiles.views import  (registro, login_view, CustomLogoutView,MiPerfilUpdateView,
                             agregar_avatar, about , mensajes_privados,DetailsMs,CanalDetailView,
                             Inbox,crear_canal,eliminar_usuario)




urlpatterns = [
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('editar-mi-perfil/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
    path("blog/",include("blog.urls")),
    path('dm/<str:username>', mensajes_privados, name = "mensajes_privados"),
    path('ms/<str:username>', DetailsMs.as_view(),name = "detailms"),
    re_path(r'canal/(?P<pk>[\w-]+)', CanalDetailView.as_view(), name = "detalle"),
    path('inbox', Inbox.as_view(), name = "inbox"),
    path('crear_canal/',crear_canal, name='crear_canal'),
    path('eliminar-perfil/<str:username>/', eliminar_usuario, name="eliminar_perfil"),

    path('about/', about, name='about'),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)