from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    product_image = models.ImageField(default="product_image.jpg")
    price = models.DecimalField(max_digits=999, decimal_places=2, blank=False)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return str(self.name)

class Advertisement(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to="images/ads")
    