from django.shortcuts import render
from projects.models import Project


def list_views(request):
    project = Project.objects.all()
    context = {
        "list_view": project,
    }
    return render(request, "project_list.html", context)
