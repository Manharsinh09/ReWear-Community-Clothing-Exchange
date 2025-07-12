from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Categories(models.Model):
  categories_name = models.CharField(max_length=50)

  def __str__(self):
    return self.categories_name


class SubCategories(models.Model):
  subcategories_name = models.CharField(max_length=50)
  categories = models.ForeignKey(Categories,on_delete=models.CASCADE,default='')

  def __str__(self):
    return self.subcategories_name

class Product(models.Model):
  product_id = models.AutoField
  name = models.CharField(max_length=50)
  price = models.IntegerField()
  desc = models.CharField(max_length=300)
  image = models.ImageField(upload_to=("cart/image"))
  pub_date = models.DateField(default=timezone.now)
  categary = models.ForeignKey(Categories,on_delete=models.CASCADE)
  subCategary = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
  is_available = models.BooleanField(default=True)
  report_count = models.PositiveIntegerField(default=0)
  
  def __str__(self):
    return self.name