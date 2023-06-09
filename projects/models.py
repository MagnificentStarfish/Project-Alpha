from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        User,
        related_name="projects",
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
