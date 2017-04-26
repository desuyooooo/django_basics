from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=512, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
