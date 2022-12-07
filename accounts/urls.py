from django.urls import path, include
from accounts.views import user_login


urlpatterns = [
    path("login/", user_login, name="login"),
    path("projects/", include("projects.urls")),
]
