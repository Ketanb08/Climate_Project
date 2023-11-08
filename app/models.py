from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def val_climate(value):
    if(value=="hot" or value=="cold" or value=="rainy" or value=="humid"):
        return 1
    else:return 0
def val_range(value):
    if( value<100 or value>1000):
        return -1
    else:return 0
def is_valid(climate,area):
    a=val_climate(climate)
    b=val_range(area)
    if(a==0 or b==0):
        return -1
    return 1
class Climate(models.Model):
    climate=models.CharField(max_length=7,validators=[val_climate])
    temperature=models.IntegerField()
    area=models.IntegerField(validators=[val_range])
    humidity=models.IntegerField()
    chances=models.IntegerField()
    date=models.DateField()
   