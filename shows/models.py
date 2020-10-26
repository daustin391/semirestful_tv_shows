from django.db import models


class Show(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128)
    network = models.CharField(max_length=64)
    release_date = models.DateField()
    desc = models.TextField()
