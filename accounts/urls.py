from django.urls import path, include
from accounts.views import user_login, user_logout


urlpatterns = [
    path("login/", user_login, name="login"),
    path("projects/", include("projects.urls")),
    path("logout/", user_logout, name="logout"),
]
