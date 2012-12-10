# -*- coding: utf-8 -*-

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=256)         
    description = models.CharField(max_length=256)         
           
class Contact(models.Model):
    customer = models.ForeignKey(Customer)         
    name = models.CharField(max_length=256)         
    phone = models.CharField(max_length=256)         
    email = models.CharField(max_length=256)         
           

