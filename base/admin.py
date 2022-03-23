from django.contrib import admin

from .models import Product, Order, OrderItem, Plant, Profile
# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Plant)
admin.site.register(Profile)