from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Material)
admin.site.register(Rol)
admin.site.register(Historial)
admin.site.register(MaterialPrestado)