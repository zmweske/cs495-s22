from django.db import models
import datetime

# Create your models here.
class Patient(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    patient_since = models.CharField(default=datetime.date.today, max_length=30)
