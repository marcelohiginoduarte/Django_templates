from django.db import models

class post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    created_on = models.CharField(max_length=10)
