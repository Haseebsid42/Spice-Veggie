# shop/admin.py

from django.contrib import admin
from .models import Product, Vegetable, Fruit  # 👈 Make sure all are imported

admin.site.register(Product)
admin.site.register(Vegetable)
admin.site.register(Fruit)
