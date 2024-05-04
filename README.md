# Uçuş Rezervasyon ve Yönetim Uygulaması

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
git clone https://github.com/Efekannnn/airline.git

2. Bir ide aracılığıyla ile klonladığınız projeyi açın ve Sanal ortam oluşturup oluşturduğunuz sanal ortamı etkinleştirin.

komut istemini açıp projenin olduğu dosyaya eriştikten sonra komut istemine(terminale) aşağıdakileri yazın.

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
komut istemini açıp projenin olduğu dosyaya eriştikten sonra komut istemine(terminale) aşağıdakileri yazın.
python manage.py migrate

5. Sunucuyu başlatın:
komut istemini açıp projenin olduğu dosyaya eriştikten sonra komut istemine(terminale) aşağıdakileri yazın.
python manage.py runserver


## Geliştirilen Arayüzün Örnek Görsellerine  klasöründe bulunan **IMAGESOFAPP** klasöründen erişebilirsiniz.  



