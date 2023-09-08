from django.db import models

# Create your models here.



class Kobo(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=40)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
