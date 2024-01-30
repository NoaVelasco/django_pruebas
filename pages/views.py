from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})

def projects(request):
    return render(request, "pages/projects.html", {})

def experience(request):
    return render(request, "pages/experience.html", {})
