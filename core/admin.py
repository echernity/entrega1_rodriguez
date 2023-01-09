from django.contrib import admin
from .models import Category, Product

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'price', 'product_image']
    
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']


admin.site.register(Category)#, CategoryAdmin)
admin.site.register(Product)#, ProductAdmin)