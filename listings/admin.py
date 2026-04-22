from django.contrib import admin
from .models import CarMake, CarModel, Listing

# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Listing)
