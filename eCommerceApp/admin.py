from django.contrib import admin
from .models import Catagery, Products,Items, Cart, Wishlist

class product_list(admin.ModelAdmin):
    list_display = ["name", "catagery"]

class Cart_list(admin.ModelAdmin):
    list_display = ["user", "product","product_quantity"]

class Wishlist_list(admin.ModelAdmin):
    list_display = ["user", "items"]

admin.site.register(Catagery)
admin.site.register(Products, product_list)
admin.site.register(Items)
admin.site.register(Cart, Cart_list)
admin.site.register(Wishlist, Wishlist_list)
