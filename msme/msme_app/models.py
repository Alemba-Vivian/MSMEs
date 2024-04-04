from django.db import models

# Create your models here.

class MSMEquestionnaire(models.Model):
    name = models.CharField(max_length=100)
    
    phone =models.IntegerField()
    email = models.EmailField(max_length=250, blank=True)
    subcounty=models.CharField(max_length=100)
    ward=models.CharField(max_length=100)
    
    disability=models.BooleanField(default=False)  
   
    cboreg=models.BooleanField(default=False)
    groupname=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    
    groupreg=models.BooleanField(default=False)
    groupoperationalyears=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    
    
