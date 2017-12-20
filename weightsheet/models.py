from django.db import models
from django.utils import timezone

# Create your models here.
class ASV_Vessel(models.Model):

    #Relations
    #Attributes - Mandatory
    ASV_Project_Number = models.CharField(max_length=4)
    Name = models.CharField(max_length=200)
    Description = models.TextField(blank=True)
    Mass = models.FloatField(null=True)
    LCG = models.FloatField(null=True)
    TCG = models.FloatField(null=True)
    VCG = models.FloatField(null=True)

    #Attributes - Optional
    #Create_by = models.DateTimeField(default=timezone.now)
    #Update_by = models.DateTimeField(blank=True, null=True)
    

    #Object Manager
    #Custom Propreties
    #Methods
    #Meta and String

class Group_System(models.Model):
    
    #Relations
    ID_ASV= models.ForeignKey(ASV_Vessel)

    #Attributes - Mandatory
    ID_GS = models.IntegerField()
    Mass = models.FloatField(null=True,blank=True)
    LCG = models.FloatField(null=True,blank=True)
    TCG = models.FloatField(null=True,blank=True)
    VCG = models.FloatField(null=True,blank=True)

    #Attributes - Optional
    #Description = models.TextField(null=True, blank=True)

    #Object Manager
    #Custom Propreties

    #Methods
    def change_mass(self,value):
        self.Mass = value
    def change_LCG(self,value):
        self.LCG = value
    def change_TCG(self,value):
        self.TCG = value
    def change_VCG(self,value):
        self.VCG = value

    #Meta and String

class Item(models.Model):

    #Relations
    ID_ASV= models.ForeignKey(ASV_Vessel)
    ID_GS= models.ForeignKey(Group_System)

    #Attributes - Mandatory
    ID_Item = models.CharField(max_length=4)
    ASV_Item = models.CharField(max_length=3)
    Local_Group = models.IntegerField()
    Global_Group = models.IntegerField()
    Part_Name = models.CharField(max_length=32)
    Description = models.TextField()
    Quantity = models.FloatField()
    Mass = models.FloatField()
    LCG = models.FloatField()
    TCG = models.FloatField()
    VCG = models.FloatField()


    #Attributes - Optional
    #Object Manager
    #Custom Propreties

    #Methods


    #Meta and String

class Bounding_Box(models.Model):

    #Attributes - Mandatory    
    X_aft = models.FloatField()
    X_forward = models.FloatField()
    Y_starboard = models.FloatField()
    Y_portside = models.FloatField()
    Z_bottom = models.FloatField()
    Z_up = models.FloatField()

    #Attributes - Optional
    #Object Manager
    #Custom Propreties

    #Methods


    #Meta and String