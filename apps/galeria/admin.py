from django.contrib import admin
from apps.galeria.models import Fotografia

# Registadmin.ser your models here.
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada", "data_publicacao")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria", "usuario")
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
