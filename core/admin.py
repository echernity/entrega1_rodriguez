from django.contrib import admin
from .models import Category, Product, Advertisement

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'product_image']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class AdAdmin(admin.ModelAdmin):
    list_display = ['name', 'img']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Advertisement, AdAdmin)