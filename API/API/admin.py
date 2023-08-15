from django.contrib import admin
from .models import Product, Seller, Transact


admin.site.register([Product, Seller, Transact])