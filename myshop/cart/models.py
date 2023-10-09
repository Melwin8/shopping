from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    date_added=models.DateField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
       return self.products.name

    def subtotal(self):
        return self.quantity * self.products.price

class Account(models.Model):
        accnum=models.CharField(max_length=20)
        accounttype=models.CharField(max_length=20)
        accamt=models.IntegerField()
        def __str__(self):
            return self.accnum

class Order(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        products=models.ForeignKey(Product,on_delete=models.CASCADE)
        address=models.TextField()
        phone=models.CharField(max_length=100)
        order_status=models.CharField(max_length=30,default="pending")
        delivery_status=models.CharField(max_length=30,default="pending")
        noofitems=models.IntegerField()
        date_added=models.DateField(auto_now_add=True)

        def __str__(self):
            return self.user.username

        def subtotal(self):
            return self.noofitems*self.products.price





