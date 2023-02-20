from django.db import models

# Create your models here.
class account(models.Model):

    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    materials_provided = models.CharField(max_length=255)
