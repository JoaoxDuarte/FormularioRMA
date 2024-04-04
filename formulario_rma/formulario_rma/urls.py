"""formulario_rma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('rmaAdmin', views.rmaAdmin, name='rmaAdmin'),
    path('send_form_cras', views.get_form_cras, name='get_form_cras'),
    path('send_form_creas', views.get_form_creas, name='get_form_creas'),
    path('send_form_centro_pop', views.get_form_centro_pop, name='get_form_centro_pop'),
    path('test_unid/', views.test_unid),
    path('accounts/', include('django.contrib.auth.urls')),
    path('leitura_formulario/',views.read_index),
    path('admin_enviar/', views.send_form_target, name='send_form_target')
]
