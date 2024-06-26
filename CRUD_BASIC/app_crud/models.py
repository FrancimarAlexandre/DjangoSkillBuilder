from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    senha = models.CharField(max_length = 255)
    idade = models.IntegerField()

    def __str__(self):
        return self.username