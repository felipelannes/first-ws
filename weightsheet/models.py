from django.db import models
from django.utils import timezone

# Create your models here.
class ASV_Vessel(models.Model):
    ID_ASV_Vessel = models.CharField(max_length=4)
    Name = models.CharField(max_length=200)
    Description = models.TextField(blank=True)
    Mass = models.FloatField(null=True,default=None)
    LCG = models.FloatField(null=True,default=None)
    TCG = models.FloatField(null=True,default=None)
    VCG = models.FloatField(null=True,default=None)



class Item(models.Model):
    ID_Item = models.CharField(max_length=4)
    ASV_Item = models.CharField(max_length=3)
    Local_Group = models.IntegerField()
    Global_Group = models.IntegerField()
    Part_Name = models.CharField(max_length=32)
    Description = models.TextField()
    Mass = models.FloatField()
    LCG = models.FloatField()
    TCG = models.FloatField()
    VCG = models.FloatField()