from django.contrib import admin

# Register your models here.

from testapp.models import Item, Order, OrderItem   # Import your models here

# Register each model with the admin site
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)

