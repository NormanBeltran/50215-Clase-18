"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludar),
    path('bienvenido/<nombre>/<apellido>/', bienvenida),
    path('bienvenido_html/<nombre>/<apellido>/', bienvenido_html),    
    path('bienvenido_tpl/', bienvenido_template),
        
    path('bienvenido_tpl1/', bienvenido_template1),  
    path('nuevo_curso/', nuevo_curso),  
]