from datetime import date
from django.db import models

# Create your models here.
class Havaalanlari(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=32)
    
    def __str__(self):
        return f"{self.city} ({self.code})"
    

class Ucuslar(models.Model):
    origin = models.ForeignKey(Havaalanlari, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Havaalanlari, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()   
    kalkis_tarihi = models.DateField(default=date.today) 
    varis_tarihi = models.DateField(default=date.today)
    havayolu_adi = models.CharField(max_length=64, default="Default Airlines")

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"