from django.contrib import admin
from eventos.models import Evento

# Register your models here.
@admin.register(Evento)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ('codigo_i3a','titulo','activo')
    list_filter = ['activo']
    search_fields = ['codigo_i3a','titulo']
