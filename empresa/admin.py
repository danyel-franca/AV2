from django.contrib import admin

from empresa.models import Empresa, Cargo, Funcionario

admin.site.register(Empresa)
admin.site.register(Cargo)
admin.site.register(Funcionario)
