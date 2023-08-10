from django.contrib import admin
from .models import Order, OrderDish, Customer, Menu, Dish

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDish)
admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Dish)
