sinif_adi = "Bilgisayar Mühendisliği"
mevcut_ogrenci_sayisi = 0
ortalama_basar = 0.0
sinif_aktif = True
ogrenciler = [
    {"isim": "ali", "yas": 20, "not": 85},
    {"isim": "ayşe", "yas": 21, "not": 90},
    {"isim": "mehmet", "yas": 19, "not": 45},
    {"isim": "zeynep", "yas": 22, "not": 70},
    {"isim": "elif", "yas": 18, "not": 61},
    {"isim": "mert", "yas": 23, "not": 48},
    {"isim": "hasan", "yas": 22, "not": 73},
    {"isim": "fatma", "yas": 21, "not": 59},
    {"isim": "yusuf", "yas": 19, "not": 81},
    
]
mevcut_ogrenci_sayisi = len(ogrenciler)
def ogrenci_ekle():
    global mevcut_ogrenci_sayisi
    isim = input("İsim girin: ").strip()
    if isim == "":
        print("İsim boş olamaz.")
        return
    yas_girdi = input("Yaş girin: ").strip()
    not_girdi = input("Not girin: ").strip()
    yas = int(yas_girdi)
    notu = int(not_girdi)
    ogrenci = {"isim": isim, "yas": yas, "not": notu}
    ogrenciler.append(ogrenci)
    mevcut_ogrenci_sayisi += 1

    if notu >= 50:
        print(isim, "adlı öğrenci başarıyla eklendi. (Durum: Geçti)")
    else:
        print(isim, "adlı öğrenci başarıyla eklendi. (Durum: Kaldı)")

def ogrencileri_listele():
    if len(ogrenciler) == 0:
        print("Henüz öğrenci yok.")
        return

    print("Öğrenciler:")
    for ogrenci in ogrenciler:
        isim = ogrenci["isim"]
        yas = ogrenci["yas"]
        notu = ogrenci["not"]
        print("-", isim, "(", yas, "yaşında ) → Not:", notu)

def ogrenci_ara():
    aranan = input("Aramak istediğiniz öğrenci ismi: ").strip()
    if aranan == "":
        print("Arama için bir isim giriniz.")
        return

    bulundu = False
    for ogrenci in ogrenciler:
        isim = ogrenci["isim"]
        yas = ogrenci["yas"]
        notu = ogrenci["not"]

        if isim == aranan:
            print(isim, "bulundu → Yaş:", yas, "Not:", notu)
            bulundu = True
            break

    if not bulundu:
        print("Öğrenci bulunamadı.")

def istatistikler():
    if len(ogrenciler) == 0:
        print("Henüz öğrenci yok.")
        return

    notlar = []
    for ogrenci in ogrenciler:
        notlar.append(ogrenci["not"])

    ortalama = sum(notlar) / len(notlar)
    en_yuksek = max(notlar)
    en_dusuk = min(notlar)

    print("Ortalama Not:", round(ortalama, 2))
    print("En Yüksek Not:", en_yuksek)
    print("En Düşük Not:", en_dusuk)

    gecenler = []
    for ogrenci in ogrenciler:
        if ogrenci["not"] >= 50:
            gecenler.append(ogrenci["isim"])

    kareler = []
    for not_degeri in notlar:
        kareler.append(not_degeri ** 2)

    print("Geçen Öğrenciler:", gecenler)
    print("Notların Kareleri:", kareler)

    isimler_set = set()
    for ogrenci in ogrenciler:
        isimler_set.add(ogrenci["isim"])

    print("Tekrarsız İsimler:", isimler_set)

while True:
    print("\n=== Öğrenci Yönetim Sistemi ===")
    print("1. Öğrenci Ekle")
    print("2. Öğrencileri Listele")
    print("3. Öğrenci Ara")
    print("4. İstatistikler")
    print("5. Çıkış")

    secim = input("Seçiminiz: ").strip()

    if secim == "":
        continue
    elif secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        ogrencileri_listele()
    elif secim == "3":
        ogrenci_ara()
    elif secim == "4":
        istatistikler()
    elif secim == "5":
        print("Programdan çıkıldı")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        continue

