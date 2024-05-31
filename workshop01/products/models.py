from django.db import models


class Product(models.Model):
    """Represents a product in the marketplace"""
    name = models.CharField(max_length=155)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=100)
    images = models.ImageField(blank=True, null=True, upload_to='products/')

    def __str__(self):
        return self.name
