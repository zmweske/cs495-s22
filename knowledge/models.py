from django.db import models

# Create your models here.
class Solution(models.Model):
    flag = models.CharField(unique=True, max_length=50)
    description = models.TextField()
    vulnerable_code = models.TextField(default=" ")
    fixed_code = models.TextField(default=" ")
    tokens = models.JSONField()
    source = models.CharField(max_length=50)
    mod_source = models.CharField(max_length=50)
    solved = models.BooleanField(default=False)
    fixed = models.BooleanField(default=False)