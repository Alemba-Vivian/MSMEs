from django.db import models

# Create your models here.
class ExternalStakeholder(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    sub_county = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    member_of_group = models.BooleanField()
    group_name = models.CharField(max_length=255, blank=True)
    membership_position = models.CharField(max_length=100)
    group_registered = models.BooleanField()
    group_operational_years = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.email
