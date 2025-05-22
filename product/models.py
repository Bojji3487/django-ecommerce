from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)  

    product_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='static/products')
    stock=models.IntegerField(max_length=200)
    

    def __str__(self):
        return self.product_name

