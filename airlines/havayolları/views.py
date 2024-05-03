import json
from pyexpat.errors import messages
import time
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render , redirect
from .models import Ucuslar, YolcuUcuslari, Yolcular


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
    
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Yolcular

def bilet_kaydet(request):
    if request.method == 'POST':
        isim = request.POST.get('isim')
        soyisim = request.POST.get('soyisim')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        pasaport_no = request.POST.get('pasaport_no')
        kart_no = request.POST.get('kart_no')
        son_kullanma = request.POST.get('son_kullanma')
        cvv = request.POST.get('cvv')
        
        if isim and soyisim and dogum_tarihi and pasaport_no and kart_no and son_kullanma and cvv:
            # yolcu bilgilerini kaydetme
            yeni_yolcu = Yolcular(isim=isim, soyisim=soyisim, dogum_tarihi=dogum_tarihi, pasaport_no=pasaport_no)
            yeni_yolcu.save()            
            ucus = Ucuslar.objects.get(pk=1)             
            # Yolcu-Uçuş ilişkisi
            yolcu_ucus = YolcuUcuslari(yolcu=yeni_yolcu, ucus=ucus) #modelsteki yolcucuslarınada veri kaydedilir.
            yolcu_ucus.save()
            return HttpResponseRedirect('/')  # 
        else:
            messages.error(request, 'Tüm alanları doldurun.')
    # Gerekli tüm alanlar doldurulmadığında veya başka bir hata olduğunda, tekrar bilet alma sayfasını göster
    return render(request, 'bilet_al.html')





