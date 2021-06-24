from django.contrib import admin

from Products.models import Product, ProductImages


class ProductImageInline(admin.TabularInline):
    model = ProductImages
    max_num = 10
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]

