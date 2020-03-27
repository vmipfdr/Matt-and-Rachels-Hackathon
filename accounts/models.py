from django.db import models

# possibly build out admin and business user

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.TextField(max_length=100)
