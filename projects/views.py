from django.shortcuts import render, redirect, get_object_or_404
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
<<<<<<< HEAD
    if request.method == "POST":
        form=ProjectForm(request.POST, request.FILES,)
        if form.is_valid():
            project = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            project.save()
            return redirect('project_detail', pk=project.pk)   
    else:
        form = ProjectForm()
    return render(request, 'projects/project_edit.html', {'form':form})

def project_edit(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('project_detail',pk=project.pk)
    else:
        form=ProjectForm(instance=project)
        return render(request, 'projects/project_edit.html', {'form':form})
=======
    form=ProjectForm()
    return render(request, 'projects/project_edit.html', {'form':form})
>>>>>>> 4db0e225bfb33b97bc6fd4bf0f12b4ce03fde929
