from django.urls import path
from projects.views import list_view, show_project, create_project

urlpatterns = [
    path("", list_view, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
]
