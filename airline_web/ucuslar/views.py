from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Flight, Passengers

# Create your views here.
def anasayfa(request):
    return render(request, "flights/anasayfa.html", {
        "flights": Flight.objects.all()
    })
def list_flight(request):
    return render(request, "flights/list.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    } )
