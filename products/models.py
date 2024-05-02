from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    content = models.TextField(max_length= 200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='products')
    def __str__(self):
        return self.title