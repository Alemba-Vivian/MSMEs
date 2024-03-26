from django.db import models

# Create your models here.

class MSMEquestionnaire(models.Model):
    name = models.CharField(max_length=100)
    
    phone =models.IntegerField()
    email = models.EmailField(max_length=250, blank=True)
    subcounty=models.CharField(max_length=100)
    ward=models.CharField(max_length=100)
    disability=models.models.BooleanField(_("Disabled"),default=False)  # Indicates if the user is disabled or not
    cboreg=models.BooleanField(_("Disabled"),default=False)
    position=models.CharField(max_length=100)
    groupreg=models.BooleanField(_("Disabled"),default=False)
    groupoperationalyears=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    
    
