from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class CrimeReports(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, blank=True)
    email_address = models.CharField(max_length=60, blank=True)
    crime_type = models.CharField(max_length=60, blank=True)
    location = models.CharField(max_length=60, blank=True)
    description = models.TextField(max_length=225, blank=True)
    evidence = models.FileField(upload_to='evidence/')
    status = models.BooleanField(True,  default=False)

