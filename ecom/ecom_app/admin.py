from django.contrib import admin
from . models import products

# Register your models here.
@admin.register(products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_img']