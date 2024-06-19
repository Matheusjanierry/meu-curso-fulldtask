from django.contrib import admin

from .models import *

admin.site.register(Paciente)
admin.site.register(Doutor)
admin.site.register(Resultado)
admin.site.register(Procedimentos)


