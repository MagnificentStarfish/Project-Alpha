from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required
def list_view(request):
    project = Project.objects.filter(owner=request.user)
    context = {
        "list_view": project,
    }
    return render(request, "project_list.html", context)


@login_required
def show_project(request, id):
    project = Project.objects.get(id=id)
    context = {
        "show_project": project,
    }
    return render(request, "projects/detail.html", context)
