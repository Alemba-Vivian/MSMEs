from django.db import models

# Create your models here.

class MSMEquestionnaire(models.Model):
    # name = models.CharField(max_length=100)
    
    # phone =models.IntegerField()
    # email = models.EmailField(max_length=250, blank=True)
    # subcounty=models.CharField(max_length=100)
    # ward=models.CharField(max_length=100)
    
    # disability=models.BooleanField(default=False)  
   
    # cboreg=models.BooleanField(default=False)
    # groupname=models.CharField(max_length=100)
    # position=models.CharField(max_length=100)
    
    # groupreg=models.BooleanField(default=False)
    # groupoperationalyears=models.CharField(max_length=100)
    Group_operation_choices=[
        ('0-1 year','0-1 year'),
         ('1-2 years','1-2 years'),
          ('Above 2 years','Above 2 years'),
        
    ]
    name = models.CharField(max_length=100)
    phone =models.IntegerField()
    email = models.EmailField(max_length=250, blank=True)
    subCounty=models.CharField(max_length=100)
    ward=models.CharField(max_length=100)
    
    disability=models.BooleanField(default=False)  
   
    chama=models.BooleanField(default=False)
    nameOfChama=models.CharField(max_length=100)
    membershipPosition=models.CharField(max_length=100)
    
    isChamaRegistered=models.BooleanField(default=False)
    chamaOperation=models.CharField(max_length=20,choices=Group_operation_choices)
    def __str__(self):
        return self.name
    
    
    
