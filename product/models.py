from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("Product Name",max_length=255)
    description = models.CharField("Description",max_length=500)
    category = models.CharField("Category Name",max_length=50,default="")
    created_at = models.DateTimeField("Created Date") 