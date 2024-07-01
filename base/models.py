from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    criado = models.DateTimeField(auto_now_add=True)