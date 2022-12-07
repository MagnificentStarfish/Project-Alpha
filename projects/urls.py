from django.urls import path
from projects.views import list_views

urlpatterns = [
    path("", list_views, name="list_projects"),
]
