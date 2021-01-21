# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Customer(models.Model):
    #One to one relationship means that a user can only have one customer and a customer can only be one user
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def__str__(self):
        return self.name

#Add cloudinary imagefield to the product model later on 
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()       
    digital = models.BooleanField(default=False, null=True, blank=False) 

    def__str__(self):
        return self.name

#Order object will have ManyToOne relationship with a customer aka ForeignKey. 
# Order will be the summary of items ordered and a transaction id
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)#Checks if customer wants to checkout or not
    transaction_id = models.CharField(max_length=200, null=True)

    def__str__(self):
        return str(self.id)

#OrderItem will have individual product items..
        
