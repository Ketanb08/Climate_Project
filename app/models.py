from django.db import models

# Create your models here.
class Climate(models.Model):
    climate=models.CharField(max_length=5)
    temperature=models.CharField(max_length=3)
    area=models.CharField(max_length=5)
    humidity=models.CharField(max_length=2)
    chances=models.CharField(max_length=2)
    date=models.DateField()