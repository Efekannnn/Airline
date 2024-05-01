from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Ucuslar

# Create your views here.

def index(request):
    return render(request, "index.html", {
        "ucuslar": Ucuslar.objects.all()
    })