from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.BooleanField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.id}'

    class Meta:
        ordering = ['created_at']


class Words(models.Model):
    word = models.CharField(max_length=8)
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, null=False, related_name="creator_user")
    activated = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.word} {self.id}"

    class Meta:
        ordering = ['created_at']


class Invitation(models.Model):
    host_user = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=False, related_name='host_user')
    guest_user = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=False, related_name='guest_user')
    response = models.BooleanField(default=False, blank=True)
    answered = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"{self.host_user.username} invites {self.guest_user.username}"
