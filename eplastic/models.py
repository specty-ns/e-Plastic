from django.db import models

# Create your models here.
class Master(models.Model):
    role = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.BigIntegerField(default=123)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default = True)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    master_id=models.ForeignKey(Master,on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    gender = models.CharField(max_length=50)

class Company(models.Model):
    master_id=models.ForeignKey(Master,on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=50)
    comp_address = models.CharField(max_length=500)
    comp_contact = models.CharField(max_length=50)
    owner_fname = models.CharField(max_length=50)
    owner_lname = models.CharField(max_length=50)
   
class PlasticC(models.Model):
    master_id=models.ForeignKey(Master,on_delete=models.CASCADE)
    pc_fname = models.CharField(max_length=50)
    pc_address = models.CharField(max_length=50)
    pc_contact = models.CharField(max_length=50)
    
