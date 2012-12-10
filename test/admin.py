# -*- coding: utf-8 -*-

from django.contrib import admin
from sample.crm import models

class CustomerAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass




admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Contact, ContactAdmin)

