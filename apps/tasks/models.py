from django.db import models
from apps.users.models import UserAccount

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    deadline = models.DateField(
        blank=True, null=True, auto_now=False, auto_now_add=False)
    creator = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
