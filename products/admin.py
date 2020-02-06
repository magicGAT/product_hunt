from django.contrib import admin
from .models import Product

# Register your models here.
# (registers DB models into the admin page)

admin.site.register(Product)
