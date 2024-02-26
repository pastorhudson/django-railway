from django.db import models


class Signup(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
