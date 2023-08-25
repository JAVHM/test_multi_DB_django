from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
