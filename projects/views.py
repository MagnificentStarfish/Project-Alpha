from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required
def list_views(request):
    project = Project.objects.filter(owner=request.user)
    context = {
        "list_view": project,
    }
    return render(request, "project_list.html", context)
