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
    contact = models.BigIntegerField()
    address = models.CharField(max_length=500)
    gender = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50,default="")
    postalcode = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to="customerimg/")


class Company(models.Model):
    master_id=models.ForeignKey(Master,on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=50)
    comp_address = models.CharField(max_length=500)
    comp_contact = models.BigIntegerField()
    comp_image = models.ImageField(upload_to="companyimg/")
    comp_fb = models.CharField(max_length=1000)
    comp_insta = models.CharField(max_length=1000)
    comp_linkedin = models.CharField(max_length=1000)
    comp_twitter = models.CharField(max_length=1000) 
    comp_website = models.CharField(max_length=200)
    owner_fname = models.CharField(max_length=50)
    owner_lname = models.CharField(max_length=50)
    owner_gender = models.CharField(max_length=50)
    owner_contact = models.CharField(max_length=50)
    owner_email = models.EmailField(max_length=50)
    

   
class PlasticC(models.Model):
    master_id=models.ForeignKey(Master,on_delete=models.CASCADE)
    pc_name = models.CharField(max_length=50)
    pc_address = models.CharField(max_length=50)
    pc_contact = models.BigIntegerField()
    pc_image = models.ImageField(upload_to="plasticcimg/")
    pc_fb = models.CharField(max_length=1000)
    pc_insta = models.CharField(max_length=1000)
    pc_linkedin = models.CharField(max_length=1000)
    pc_twitter = models.CharField(max_length=1000) 
    pc_website = models.CharField(max_length=200)
    owner_fname = models.CharField(max_length=50)
    owner_lname = models.CharField(max_length=50)
    owner_gender = models.CharField(max_length=50)
    owner_contact = models.BigIntegerField(default=0000000000)
    owner_email = models.EmailField(max_length=50)

class PlasticProduct(models.Model):
    plasticc_id=models.ForeignKey(PlasticC,on_delete=models.CASCADE)
    pproduct_name = models.CharField(max_length=100)
    pproduct_date = models.DateTimeField()
    pproduct_price = models.BigIntegerField(default=0)
    pproduct_image = models.ImageField(upload_to="pproductimg/")
    pproduct_quantity = models.BigIntegerField(default=0)

class RecycleProduct(models.Model):
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    rproduct_name = models.CharField(max_length=100)
    rproduct_date = models.DateTimeField()
    rproduct_price = models.BigIntegerField(default=0)
    rproduct_image = models.ImageField(upload_to="rproductimg/")
    rproduct_quantity = models.BigIntegerField(default=0)
    rproduct_desc = models.CharField(max_length=500)

class RequestButton(models.Model):
    comp_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    plasticc_id=models.ForeignKey(PlasticC,on_delete=models.CASCADE)
    pproduct_id=models.ForeignKey(PlasticProduct,on_delete=models.CASCADE)
    request_date = models.DateTimeField()
    request_quantity = models.BigIntegerField(default=0)

class AddToCart(models.Model):
    rp_id=models.ForeignKey(RecycleProduct,on_delete=models.CASCADE)
    cust_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    cart_price=models.BigIntegerField(default=0)
    cart_quantity=models.BigIntegerField(default=1)
    cart_date=models.DateTimeField()
    cart_subtotal=models.BigIntegerField(default=0)

class Checkout(models.Model):
    cart_id=models.ForeignKey(AddToCart,on_delete=models.CASCADE)
    order_total=models.BigIntegerField(default=0)
    