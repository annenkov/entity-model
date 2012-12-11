class ContactAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', 'phone', 'email',)


