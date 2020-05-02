from django.db import models


# Create your models here.

class Details(models.Model):
    id=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
