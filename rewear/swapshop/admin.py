from django.contrib import admin
from .models import Product,Categories,SubCategories
# Register your models here.



admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(SubCategories)

