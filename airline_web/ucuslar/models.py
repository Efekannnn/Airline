from datetime import date
from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32, default="country")
    
    
    def __str__(self):
        return f"{self.city} ({self.code}) {self.country}"
    

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()   
    kalkis_tarihi = models.DateField(default=date.today) 
    varis_tarihi = models.DateField(default=date.today)
    havayolu_adi = models.CharField(max_length=64, default="Default Airlines")

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
class Passengers(models.Model):
    first = models.CharField(max_length=32)
    last = models.CharField(max_length=32)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"

SEAT_CLASS = (
    ('economy', 'Economy'),
    ('business', 'Business')
)
    
class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets")
    passenger = models.ForeignKey(Passengers, on_delete=models.CASCADE, related_name="tickets")
    seat_class = models.CharField(max_length=32, choices=SEAT_CLASS)  

    def __str__(self):
        return f"Ticket for {self.passenger} on Flight {self.flight} ({self.seat_class})"


    