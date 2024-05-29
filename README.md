# Uçuş Rezervasyon ve Yönetim Uygulaması
# Uçuş Arama
![image](https://github.com/Efekannnn/airline-automation-website/assets/139994163/5ce12d4d-9ded-46ae-886b-09d09a403eb8)
# Bilet Al
![image](https://github.com/Efekannnn/airline-automation-website/assets/139994163/13b1dfd6-f5d9-474b-a488-2155a14c4efc)
# Bilet Al
![image](https://github.com/Efekannnn/airline-automation-website/assets/139994163/225a0f34-2e05-4b93-944c-2464090af32d)
# İletişim
![image](https://github.com/Efekannnn/airline-automation-website/assets/139994163/4d1dd363-31db-417c-9cd9-b9c390bd3c5e)

Bu uygulama, bir bilet satış ve yönetim platformudur. Uygulama kullanıcıların uçuşları aramasına, bilet rezervasyonu yapmasına ve yöneticilerin satılan biletleri yönetmesine olanak tanır.

## Özellikler

- Kullanıcılar, uçuşları tarih, varış ve kalkış noktalarına göre arayabilir.
- Uygun uçuşları bulduktan sonra, kullanıcılar bilet rezervasyonu yapabilir.
- Yöneticiler, bilet satışlarını ve rezervasyonları yönetebilir, iptal edebilir ve güncelleyebilir.
- Admin paneli aracılığıyla sistem yöneticileri, uçuşları, havaalanlarını ve diğer sistem ayarlarını yönetebilir.

## Kullanılan Teknolojiler

- **Django**: Güçlü bir Python web çatısı.
- **MySQL ve SQLite**: Veritabanı yönetimi için kullanılan ilişkisel veritabanı yöneticileri.
- **Bootstrap**: Hızlı ve duyarlı web tasarımı için popüler CSS kütüphanesi.
- **HTML, CSS ve JavaScript**: Temel web teknolojileri.

## Kurulum

1. Projeyi klonlayın:

Komut istemini(terminali) açın ve alttaki kodu yazarak uygulamayı klonlayın. 
git clone https://github.com/Efekannnn/airline-automation-website.git

2. Bir ide aracılığıyla ile klonladığınız projeyi açın ve Sanal ortam oluşturup oluşturduğunuz sanal ortamı etkinleştirin.

Komut istemini açıp projenin olduğu dosyaya eriştikten sonra komut istemine(terminale) aşağıdakileri yazın.

Unix/Linux veya MacOs için:
python3 -m venv myenv
source myenv/bin/activate

Windows için: 
py -m venv env
.\env\Scripts\activate

3. Gerekli bağımlılıkları yükleyin:
   
pip freeze > requirementstxt
pip install -r requirements.txt(bu dosya boş gelirse ekler bölmesinde bulunan rquirments.txt dosyasının içindeki yazıları bu dosyaya kopyalayın)

4. Veritabanını migrate edin:
   
Komut istemini açıp projenin olduğu dosyaya eriştikten sonra komut istemine(terminale) aşağıdakileri yazın.
python manage.py migrate

5. Sunucuyu başlatın:
   
Komut istemini açıp projenin olduğu dosyaya eriştikten sonra komut istemine(terminale) aşağıdakileri yazın.
python manage.py runserver

6. Admin belirleyin:

Komut istemciyi açıp python manage.py createsuperuser komutu ile admin belirleyin ve artık http://127.0.0.1:8000/admin/ bağlantısından admin girişi yapabilirsiniz.

## Geliştirilen Arayüzün Diğer Örnek Görsellerine ekler klasöründe bulunan **IMAGESOFAPP** klasöründen erişebilirsiniz.  



