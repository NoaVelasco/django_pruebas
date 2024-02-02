from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Experience, Persona
from .forms import PersonaForm, ExperienceForm

# Create your views here.
def home(request):
    persona = Persona.objects.get(id=1)
    return render(request, "pages/home.html", {'bio': persona})

def home_edit(request):
    persona = Persona.objects.get(id=1)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            return redirect('home')
    else:
            form=PersonaForm(instance=persona)
            return render(request, 'pages/home_edit.html', {'form':form})

def experience(request):
    exps = Experience.objects.filter(persona__exact=1)
    bio = Persona.objects.get(id=1)
    return render(request, "pages/experience.html", {'exps': exps,'bio': bio})

