from django.shortcuts import render, redirect
from .mongo_connection import get_db
from datetime import datetime

def index(request):
    return render(request, "index.html")

def registrar_catequizando(request):
    if request.method == "POST":
        db = get_db()
        catequizandos = db["catequizandos"]

        nuevo = {
            "cedula": request.POST.get("cedula"),
            "nombres": request.POST.get("nombres"),
            "apellidos": request.POST.get("apellidos"),
            "telefono": request.POST.get("telefono"),
            "parroquia": request.POST.get("parroquia"),
            "curso": request.POST.get("curso")
        }

        catequizandos.insert_one(nuevo)
        return redirect("listar_catequizandos")

    return render(request, "registro_catequizando.html")


def listar_catequizandos(request):
    db = get_db()
    catequizandos = db["catequizandos"]

    lista = list(catequizandos.find())

    return render(request, "listar_catequizandos.html", {"catequizandos": lista})

def consultar_por_parroquia(request):
    resultados = []
    parroquia_busqueda = ""

    if request.method == "POST":
        parroquia_busqueda = request.POST.get("parroquia")
        db = get_db()
        coleccion = db["catequizandos"]

        resultados = list(coleccion.find({"parroquia": parroquia_busqueda}))

    return render(request, "consulta_parroquia.html", {
        "resultados": resultados,
        "parroquia": parroquia_busqueda
    })


def consultar_por_curso(request):
    resultados = []
    curso_busqueda = ""

    if request.method == "POST":
        curso_busqueda = request.POST.get("curso")
        db = get_db()
        coleccion = db["catequizandos"]

        resultados = list(coleccion.find({"curso": curso_busqueda}))

    return render(request, "consulta_curso.html", {
        "resultados": resultados,
        "curso": curso_busqueda
    })



def registrar_asistencia(request):
    if request.method == "POST":
        db = get_db()
        asistencias = db["asistencias"]

        nueva_asistencia = {
            "cedula": request.POST.get("cedula"),
            "curso": request.POST.get("curso"),
            "fecha": request.POST.get("fecha"),
            "estado": request.POST.get("estado"),
            "observacion": request.POST.get("observacion"),
        }

        asistencias.insert_one(nueva_asistencia)

        return redirect("listar_asistencias")

    return render(request, "registro_asistencia.html")


def listar_asistencias(request):
    db = get_db()
    asistencias = db["asistencias"]

    lista = list(asistencias.find())

    return render(request, "listar_asistencias.html", {
        "asistencias": lista
    })

def consultar_asistencias_por_cedula(request):
    resultados = []
    cedula_busqueda = ""

    if request.method == "POST":
        cedula_busqueda = request.POST.get("cedula")

        db = get_db()
        asistencias = db["asistencias"]

        resultados = list(asistencias.find({"cedula": cedula_busqueda}))

    return render(request, "consulta_asistencia_cedula.html", {
        "resultados": resultados,
        "cedula": cedula_busqueda
    })

def reporte_asistencia_por_persona(request):
    resumen = []
    cedula_busqueda = ""

    if request.method == "POST":
        cedula_busqueda = request.POST.get("cedula")

        db = get_db()
        asistencias = db["asistencias"]

        pipeline = [
            {"$match": {"cedula": cedula_busqueda}},
            {
                "$group": {
                    "_id": "$estado",
                    "total": {"$sum": 1}
                }
            }
        ]

        resultado = list(asistencias.aggregate(pipeline))

        # Convertir a formato fácil para HTML
        conteos = {
            "Asistió": 0,
            "Falta": 0,
            "Justificado": 0
        }

        for r in resultado:
            conteos[r["_id"]] = r["total"]

        resumen = conteos

    return render(request, "reporte_asistencia_persona.html", {
        "cedula": cedula_busqueda,
        "resumen": resumen
    })

def reporte_asistencia_por_curso(request):
    curso_busqueda = ""
    resultados = []

    if request.method == "POST":
        curso_busqueda = request.POST.get("curso")

        db = get_db()
        asistencias = db["asistencias"]

        pipeline = [
            {"$match": {"curso": curso_busqueda}},
            {
                "$group": {
                    "_id": "$estado",
                    "total": {"$sum": 1}
                }
            }
        ]

        resultados = list(asistencias.aggregate(pipeline))

    return render(request, "reporte_asistencia_curso.html", {
        "curso": curso_busqueda,
        "resultados": resultados
    })
