from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Catagery(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to='media/catagery/', null=False, blank=False)
    status = models.BooleanField( max_length=50, default=True, help_text="0-hide, 1-show")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Products(models.Model):
    catagery = models.ForeignKey(Catagery, verbose_name=("Products"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to='media/products/', null=False, blank=False )
    status = models.BooleanField( max_length=50, default=True, help_text="0-hide, 1-show")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Items(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, null=False, blank=False)
    vendor = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to='static/media/items', null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    old_price = models.DecimalField( max_digits=50, decimal_places=2, null=True, blank=True)
    new_price = models.DecimalField( max_digits=50, decimal_places=2)
    description = models.CharField( max_length=500)
    highlights1 = models.CharField(max_length=255,null=True, blank=True)
    highlights2 = models.CharField(max_length=255,null=True, blank=True)
    highlights3 = models.CharField(max_length=255,null=True, blank=True)
    highlights4 = models.CharField(max_length=255,null=True, blank=True)
    highlights5 = models.CharField(max_length=255,null=True, blank=True)
    status = models.BooleanField( default=True, help_text="0-hide, 1-show")
    trending = models.BooleanField(default=False, help_text="0-hide, 1-show")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def offer(self):
        old = int(self.old_price)
        new = int(self.new_price)
        discount = old-new
        offer_percentage = round((discount/old) * 100)
        return offer_percentage
    


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey( Items , on_delete=models.CASCADE)
    product_quantity  = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_quantity * self.product.new_price
    

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    