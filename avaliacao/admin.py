from django.contrib import admin
from .models import Colaborador, Criterio, Avaliacao, Nota

# Register your models here.

admin.site.register(Colaborador)
admin.site.register(Criterio)
admin.site.register(Avaliacao)
admin.site.register(Nota)

