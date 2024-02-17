from django.db import models
from flight.models import User

# Create your models here.
class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    number_of_stars = models.IntegerField()
    has_single_rooms = models.BooleanField(default=False)
    has_double_rooms = models.BooleanField(default=False)
    has_deluxe_rooms = models.BooleanField(default=False)
    has_suites = models.BooleanField(default=False)
    has_presidential_suites = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hotel_name} in {self.city}, {self.number_of_stars} stars"
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    ROOM_TYPE_CHOICES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('deluxe', 'Deluxe Room'),
        ('suite', 'Suite'),
        ('presidential_suite', 'Presidential Suite'),
    ]
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username} reserved {self.room_type} at {self.hotel.hotel_name} on {self.check_in_date}"