# -*- coding: utf-8 -*-

from django.contrib import admin
from sample.crm import models

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', 'phone', 'email',)




admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Contact, ContactAdmin)

