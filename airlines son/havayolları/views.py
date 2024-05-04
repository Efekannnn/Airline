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
    


def bilet_kaydet(request):
     if request.method == 'POST':
        isim = request.POST.get('isim')
        soyisim = request.POST.get('soyisim')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        pasaport_no = request.POST.get('pasaport_no')
        
        # Tüm gerekli alanların dolu olduğunu kontrol et
        if isim and soyisim and dogum_tarihi and pasaport_no:
            #veritabanına kaydededer
            yolcu = Yolcular(isim=isim, soyisim=soyisim, dogum_tarihi=dogum_tarihi, pasaport_no=pasaport_no)
            yolcu.save()

            ucus = Ucuslar.objects.get(pk=1)   #yolcuların bilgisini yolcuucusları veritabanına kaydederiz.
            yolcu_ucus = YolcuUcuslari.objects.create(yolcu=yolcu, ucus=ucus)
           
            return redirect('/')  # bilet alındıktan sonra ana sayfaya yönlendir
        else:
            return render(request,'bilet_al.html')

     return render(request, 'bilet_al.html')



