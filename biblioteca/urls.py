from django.contrib import admin
from django.urls import path,include
from appBiblioteca.views import base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('appBiblioteca.urls')),
]
