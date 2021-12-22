from django.contrib import admin
from .models import Product, discountCode


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class discountCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(discountCode, discountCodeAdmin)
