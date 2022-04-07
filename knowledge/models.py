from django.db import models

# Create your models here.
class Solution(models.Model):
    flag = models.CharField(unique=True, max_length=50)
    description = models.TextField()
    tokens = models.JSONField()
    source = models.CharField(max_length=50)