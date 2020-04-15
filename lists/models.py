from django.db import models

# Create your models here.
class Item(models.Model):
    items = models.Manager()
    text = models.TextField(default='')
