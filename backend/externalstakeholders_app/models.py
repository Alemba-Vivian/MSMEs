from django.db import models

# Create your models here.
class ExternalStakeholder(models.Model):
    Group_operation_choices = [
        ('0-1', '0-1 years'),
        ('1-5', '1-5 years'),
        ('5+', 'More than 5 years'),
    ]
    name = models.CharField(max_length=255)
    phone= models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    subCounty = models.CharField(max_length=100)
    diasability=models.BooleanField(default=False)
    ward = models.CharField(max_length=100)
    chama = models.BooleanField()
    nameOfChama = models.CharField(max_length=255, blank=True)
    membershipPosition = models.CharField(max_length=100)
    isChamaRegistered= models.BooleanField()
    chamaOperation = models.CharField(max_length=20,choices=Group_operation_choices)
    
    
    def __str__(self):
        return self.email
