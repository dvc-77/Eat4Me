from django.contrib import admin
from .models import Restaurant, Customer, Driver

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)