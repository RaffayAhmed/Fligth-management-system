from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    cnic = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.username

class Flights(models.Model):
    flight_number = models.CharField(max_length=20, primary_key=True)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    date = models.DateField()
    airlines = models.CharField(max_length=100)

    def __str__(self):
        return self.flight_number

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    plane_class = models.CharField(max_length=10)  # e.g., 'Economy', 'Business', etc.
    seat_number = models.CharField(max_length=10)

class Complaint(models.Model):
    complain_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"Complaint {self.complain_id} - {self.subject} from {self.name}"