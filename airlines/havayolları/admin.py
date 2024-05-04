from django.contrib import admin
from .models import Ucuslar #admine model sınıflarımızı tek tek ekleriz
from .models import Havaalanlari
from .models import Yolcular
from .models import YolcuUcuslari

admin.site.register(Ucuslar) # UCUSLAR modeli böyle eklenir
admin.site.register(Havaalanlari)
admin.site.register(YolcuUcuslari)
admin.site.register(Yolcular)

