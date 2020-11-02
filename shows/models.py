from datetime import datetime
from django.db import models


class ShowManager(models.Manager):
    def validate(self, form_data):
        errors = {}
        for key, value in form_data.items():
            if key == "release_date":
                if len(value) == 0:
                    errors[key] = "Release date field cannot be empty."
                elif datetime.now() < datetime.strptime(value, "%Y-%m-%d"):
                    errors[key] = "Release date cannot be in the future."
            elif key == "title" and len(value) < 2:
                errors[key] = "Title must be at least 2 characters."
            elif key == "network" and len(value) < 3:
                errors[key] = "Network must be at least 3 characters."
            elif key == "desc" and len(value) <= 10:
                errors[key] = "Description must be at least 10 characters."
        return errors


class Show(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128)
    network = models.CharField(max_length=64)
    release_date = models.DateField()
    desc = models.TextField()
    objects = ShowManager()
