from django.urls import path
from projects.views import list_view, show_project

urlpatterns = [
    path("", list_view, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
]
