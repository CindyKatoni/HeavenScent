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

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()       
    digital = models.BooleanField(default=False, null=True, blank=False) 

    def__str__(self):
        return self.name