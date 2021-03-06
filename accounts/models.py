import uuid
from django.contrib import auth
from django.db import models

class User(models.Model):
    objects = models.Manager()

    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True

class Token(models.Model):
    objects = models.Manager()

    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=40)
