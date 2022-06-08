from django.db import models

# Create your models here.
class Space(models.Model):
    room=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    guests=models.IntegerField(default=0)