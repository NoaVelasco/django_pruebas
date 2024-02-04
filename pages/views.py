from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from projects.models import Experience, Persona
from .forms import PersonaForm, ExperienceForm


# Create your views here.
def index(request):
    portfolios = Persona.objects.all()
    return render(request, "pages/index.html", {"portfolios": portfolios})


def bio(request, pk):
    bio = Persona.objects.get(pk=pk)
    return render(request, "pages/bio.html", {"bio": bio})


def bio_edit(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            reverse_path = reverse("bio", args=[pk])
            return redirect(reverse_path)
            # return redirect("bio", pk=pk)
    else:
        form = PersonaForm(instance=persona)
        return render(
            request, "pages/bio_edit.html", {"form": form, "portfolio": persona}
        )


def exp(request, pk):
    exps = Experience.objects.filter(persona__exact=pk)
    return render(request, "pages/exp.html", {"pk": pk, "exps": exps})


def exp_edit(request, pk_exp):
    exp = get_object_or_404(Experience, pk=pk_exp)
    persona = exp.persona_id
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            exp = form.save(commit=True)
            exp.save()
            reverse_path = reverse("exp", args=[persona])
            return redirect(reverse_path)
            # return redirect("home")
    else:
        form = ExperienceForm(instance=exp)
        return render(
            request,
            "pages/exp_edit.html",
            {"form": form, "exp": exp},
        )


# OLDS --------------------------------
# def home(request):
#     persona = Persona.objects.get(id=1)
#     return render(request, "pages/home.html", {"bio": persona})


# def home_edit(request):
#     persona = Persona.objects.get(id=1)
#     if request.method == "POST":
#         form = PersonaForm(request.POST, instance=persona)
#         if form.is_valid():
#             persona = form.save(commit=False)
#             persona.save()
#             return redirect("home")
#     else:
#         form = PersonaForm(instance=persona)
#         return render(request, "pages/home_edit.html", {"form": form})


# def experience(request):
#     exps = Experience.objects.all()
#     # bio = Persona.objects.get(id=1)
#     return render(request, "pages/experience.html", {"exps": exps})


# def experience_edit(request, pk):
#     experience = get_object_or_404(Experience, pk=pk)
#     if request.method == "POST":
#         form = ExperienceForm(request.POST, instance=experience)
#         if form.is_valid():
#             experience = form.save(commit=True)
#             experience.save()
#             return redirect("home")
#     else:
#         form = ExperienceForm(instance=experience)
#         return render(request, "pages/experience_edit.html", {"form": form})
