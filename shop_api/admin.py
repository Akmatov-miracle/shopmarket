from django.contrib import admin

from shop_api.models import Category, Product, Like, Favorite, Cart

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Like)
admin.site.register(Favorite)
admin.site.register(Cart)
