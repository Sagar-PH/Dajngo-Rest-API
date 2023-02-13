from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Book(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=40, null=False)
    author=models.CharField(max_length=100, default=' ')
    publisher=models.CharField(max_length=100, default=' ')
    published=models.DateTimeField(auto_now_add=True)
    summary=models.TextField(max_length=400)

    def __str__(self):
        return self.title