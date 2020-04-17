from django.db import models

# Create your models here.
class List(models.Model):
    lists = models.Manager()
    
class Item(models.Model):
    items = models.Manager()
    text = models.TextField(default='') 
    list = models.ForeignKey(List, on_delete=models.CASCADE)

