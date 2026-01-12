from django.contrib import admin
from django.urls import path
from catequesis_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="inicio"),
    path("catequizandos/nuevo/", views.registrar_catequizando, name="registrar_catequizando"),
    path("catequizandos/listar/", views.listar_catequizandos, name="listar_catequizandos"),
]
