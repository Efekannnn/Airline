
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect
from .models import Ucuslar, Yolcular


def anasayfa(request):
    return render(request, 'havayolları/index.html', {
        "ucuslar": Ucuslar.objects.all()
    })



def flight_search(request):
    if request.method == 'GET':
        from_airport = request.GET.get('from_airport')
        to_airport = request.GET.get('to_airport')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        ##uçuş filtreleme
        flights = Ucuslar.objects.filter(
            kalkis_havaalani_id=from_airport,
            varis_havaalani_id=to_airport,
            kalkis_tarihi=start_date,
            varis_tarihi=end_date
        )

        return render(request, 'flight_search.html', {'flights': flights})
    else:
        return render(request, 'flight_search.html', {'flights': None})
    

def bilet_al(request):
    return render(request, 'havayolları/bilet_al.html')


def kart_bilgisi_gir(request):
    return render(request, 'havayolları/kart_bilgisi_gir.html')


