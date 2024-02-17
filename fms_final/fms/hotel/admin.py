from django.contrib import admin

# Register your models here.
from .models import Hotels, Reservation

admin.site.register(Hotels)
admin.site.register(Reservation)