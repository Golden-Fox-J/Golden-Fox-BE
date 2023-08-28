from django.contrib import admin
from .models import Category,Product,Comment,Favourite_product,Cart,CartItem

# Register your models here.
admin.site.register([Category,Product,Comment,Favourite_product,Cart,CartItem])
