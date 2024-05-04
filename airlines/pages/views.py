from django.http import HttpResponse
from django.shortcuts import render

def iletisim(request):
    return render(request, 'pages/iletisim.html')

def submit_form(request):
    if request.method == 'POST':
        # form verilerini alırız
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        message = request.POST.get('message', '')

        return HttpResponse(f'Mesajınız alındı. En Kısa sürede dönüş yapılacaktır.')
    else:
        return HttpResponse('Hatalı gönderim.')

def hakkimizda(request):
    return render(request, 'pages/hakkimizda.html')

