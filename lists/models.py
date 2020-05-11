from django.db import models
from django.urls import reverse

# Create your models here.
class List(models.Model):
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    
class Item(models.Model):
    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    objects = models.Manager()
    text = models.TextField(default='') 
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

