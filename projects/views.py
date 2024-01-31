from django.shortcuts import render
from projects.models import Project
from .forms import ProjectForm

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "projects/project_detail.html", context)

def project_new(request):
    form=ProjectForm()
    return render(request, 'projects/project_edit.html', {'form':form})