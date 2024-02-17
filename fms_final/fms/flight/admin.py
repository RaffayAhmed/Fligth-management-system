from django.contrib import admin

# Register your models here.
from .models import User, Flights, Booking, Complaint

admin.site.register(User)
admin.site.register(Flights)
admin.site.register(Booking)
admin.site.register(Complaint)