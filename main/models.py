from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.name
    
    
class Size(models.Model):
    name = models.CharField(max_length=20)
    
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
    
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='products/main/')
    created_at = models.DateTimeField(auto_now_add=True)     
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
            
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.name
     
     
class ProductSize(models.Model):
    product = models.ForeignKey(Product, related_name='product_size', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.size} ({self.stock} in stock) for {self.product.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/extra/')