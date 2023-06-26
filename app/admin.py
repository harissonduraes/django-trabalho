from django.contrib import admin
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','periodo','nota','situacao')

admin.site.register(Aluno, AlunoAdmin)