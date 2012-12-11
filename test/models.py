# -*- coding: utf-8 -*-

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=256)         
    description = models.CharField(max_length=256)         
              
    def __unicode__(self):
        return "Customer: {0}".format(self.name)


class Contact(models.Model):
    customer = models.ForeignKey(Customer)         
    name = models.CharField(max_length=256)         
    phone = models.CharField(max_length=256)         
    email = models.CharField(max_length=256)         
              
    def __unicode__(self):
        return "Contact: {0}".format(self.pk)



