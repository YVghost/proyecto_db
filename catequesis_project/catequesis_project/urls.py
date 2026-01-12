from django.contrib import admin
from django.urls import path
from catequesis_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="inicio"),
    path("catequizandos/nuevo/", views.registrar_catequizando, name="registrar_catequizando"),
    path("catequizandos/listar/", views.listar_catequizandos, name="listar_catequizandos"),
    path("consultas/parroquia/", views.consultar_por_parroquia, name="consulta_parroquia"),
    path("consultas/curso/", views.consultar_por_curso, name="consulta_curso"),
    path("asistencias/nueva/", views.registrar_asistencia, name="registrar_asistencia"),
    path("asistencias/listar/", views.listar_asistencias, name="listar_asistencias"),
    path("asistencias/consulta/cedula/", views.consultar_asistencias_por_cedula, name="consulta_asistencia_cedula"),
    path("reportes/asistencia/persona/", views.reporte_asistencia_por_persona, name="reporte_asistencia_persona"),
    path("reportes/asistencia/curso/", views.reporte_asistencia_por_curso, name="reporte_asistencia_curso"),



]
