from django.shortcuts import render, redirect
from .mongo_connection import get_db

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
