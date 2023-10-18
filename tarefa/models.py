from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    descricao = models.TextField()