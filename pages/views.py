from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})

# @NOA: La vista de PROJECTS está en la carpeta de PROJECTS
# Creo que aquí no hace nada, ¿verdad? 🤔
# def projects(request):
#     return render(request, "pages/projects.html", {})

def experience(request):
    return render(request, "pages/experience.html", {})
