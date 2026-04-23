from django.contrib import admin

from users.models import Profile
from .models import CarMake, CarModel, Listing

# Register your models here.
admin.site.register(Profile)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Listing)
