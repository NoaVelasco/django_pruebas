from django.shortcuts import render
from projects.models import Experience, Persona, Project

# Create your views here.
def home(request, pk):
    bio = Persona.objects.get(id=pk)
    return render(request, "pages/home.html", {'bio': bio})

# @NOA: La vista de PROJECTS está en la carpeta de PROJECTS
# Creo que aquí no hace nada, ¿verdad? 🤔
# def projects(request):
#     return render(request, "pages/projects.html", {})

def experience(request, pk):
    exps = Experience.objects.filter(persona__exact=pk)
    return render(request, "pages/experience.html", {'exps': exps})
