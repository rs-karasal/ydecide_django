from django.db import models
from django.contrib.auth.models import User


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_hiring = models.BooleanField(default=True)
    contact = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Mentee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, related_name='mentees')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    learning_goals = models.TextField(null=True, blank=True)
    contact = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
