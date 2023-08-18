from django.contrib import admin
from perfiles.models import Avatar, CanalMensaje, CanalUsuario, CanalQuerySet, CanalManager,Canal
# Register your models here.

class CanalMensajeInline(admin.TabularInline):
    model = CanalMensaje
    extra = 1

class CanalUsuarioInline(admin.TabularInline):
    model = CanalUsuario
    extra = 1

class CanalAdmin(admin.ModelAdmin):
    inlines = [CanalMensajeInline, CanalUsuarioInline]

    class Meta:
        model = Canal



admin.site.register(Avatar)
admin.site.register(Canal, CanalAdmin)
admin.site.register(CanalUsuario)
admin.site.register(CanalMensaje)