from django.db import models

class Ucuslar(models.Model):
    ucus_id = models.AutoField(primary_key=True)
    kalkis_havaalani_id = models.CharField(max_length=50)
    varis_havaalani_id = models.CharField(max_length=50)
    kalkis_tarihi = models.DateField()
    varis_tarihi = models.DateField()
    havayolu_adi = models.CharField(max_length=255)
    ucus_sure = models.IntegerField()
    ucak_no = models.CharField(max_length=50)

    class Meta:
        db_table = 'ucuslar'

    def __str__(self):
        return f"Uçuş ID: {self.ucus_id}, Kalkış Havalimanı ID: {self.kalkis_havaalani_id}, Varış Havalimanı ID: {self.varis_havaalani_id}"

class Yolcular(models.Model):
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=50)
    pasaport_no = models.CharField(max_length=20, unique=True)
    dogum_tarihi = models.DateField()

    class Meta:
        db_table = 'yolcular'

    def __str__(self):
        return f"{self.isim} {self.soyisim}"

class YolcuUcuslari(models.Model):
    yolcu = models.ForeignKey(Yolcular, on_delete=models.CASCADE, related_name='ucuslar')
    ucus = models.ForeignKey(Ucuslar, on_delete=models.CASCADE, related_name='yolcular')

    class Meta:
        db_table = 'yolcu_ucuslari'

    def __str__(self):
        return f"{self.yolcu} - {self.ucus}"

class Havaalanlari(models.Model):
    havaalani_ismi = models.CharField(max_length=100)
    sehir = models.CharField(max_length=100)
    ulke = models.CharField(max_length=100)

    class Meta:
        db_table = 'havaalanlari'

    def __str__(self):
        return self.havaalani_ismi
