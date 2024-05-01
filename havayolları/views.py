from django.shortcuts import render
from django.http import HttpResponse
from .models import Ucuslar #/ uçuşlar modelindeki verileri getiririz.
from django.http import HttpResponse


def anasayfa(request):
    return render(request, 'havayolları/index.html', {
        "ucuslar": Ucuslar.objects.all()
    })


