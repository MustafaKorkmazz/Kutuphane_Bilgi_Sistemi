kutuphane = {}
kullanicilar = {} 
def kitap_ekle(kutuphane,kitap_ismi,yazar,adet):
    if kitap_ismi in kutuphane:
        kutuphane[kitap_ismi]["adet"]+=adet
    else:
        kutuphane[kitap_ismi] = {"yazar": yazar, "adet": adet}
        print(f"{kitap_ismi} kitabı kütüphaneye eklendi.Toplam adet {kutuphane[kitap_ismi]["adet"]}")

def kitap_listele(kutuphane):
    if not kutuphane:
        print("Kütüphanede hiç kitap bulunmamaktadır.")
    else:
        for kitap_ismi,bilgi in kutuphane:
            print(f"{kitap_ismi}(Yazar :{bilgi["yazar"]} , Adet :{bilgi["adet"]})")

def kitap_odunc_al(kutuphane, kullanicilar, kullanici_adi, kitap_ismi):
    if kitap_ismi not in kutuphane or kutuphane[kitap_ismi]["adet"]<=0:
        print("Kütüphanede böyle bir kitap bulunmamaktadır.")
    else :
        kutuphane[kitap_ismi]["adet"]-=1
        if kullanici_adi not in kullanicilar:
            kullanicilar[kullanici_adi]=[]
            kullanicilar[kullanici_adi].append(kitap_ismi)
            print(f"{kullanici_adi}, '{kitap_ismi}' kitabını ödünç aldı.")

def kitap_iade_et(kutuphane, kullanicilar, kullanici_adi, kitap_ismi):
    if kullanici_adi not in kullanicilar or kitap_ismi not in kullanicilar[kullanici_adi]:
        print(f"{kullanici_adi}, '{kitap_ismi}' kitabını ödünç almamış.")
    else:
        kullanicilar[kullanici_adi].remove(kitap_ismi)
        kutuphane[kitap_ismi]["adet"]+=1
        print(f"{kullanici_adi} ismindeki kullanıcı {kitap_ismi} kitabını iade etti.")

def kullanici_bilgileri(kullanicilar, kullanici_adi):
    if kullanici_adi not in kullanicilar or not kullanicilar[kullanici_adi]:
            print(f"{kullanici_adi} henüz hiç kitap ödünç almamış.")
    else:
            print(f"{kullanici_adi} tarafından ödünç alınan kitaplar:")
            for kitap in kullanicilar[kullanici_adi]:
                print(f"-{kitap}")

def main():
    print("Kütüphane Yönetim Sistemi'ne Hoş Geldiniz!")
    while True:
        print("\nSeçenekler:")
        print("1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Ödünç Al")
        print("4. Kitap İade Et")
        print("5. Kullanıcı Bilgilerini Göster")
        print("6. Çıkış")

        secim = input("Bir seçenek seçin (1-6): ")
        if secim=="1":
            kitap_ismi = input("Kitap ismini girin: ")
            yazar = input("Yazar ismini girin: ")
            adet = int(input("Kitap adedini girin: "))
            kitap_ekle(kutuphane, kitap_ismi, yazar, adet)
        elif secim=="2":
            kitap_listele(kutuphane)
        elif secim=="3":
            kullanici_adi=input("Kullanıcı adınızı giriniz :")
            kitap_ismi=input("Ödünç alınacak kitabın adınızı giriniz :")
            kitap_odunc_al(kutuphane,kullanicilar,kullanici_adi,kitap_ismi)
        elif secim=="4":
            kullanici_adi=input("Kullanıcı adınızı giriniz :")
            kitap_ismi=input("İade alınacak kitabın adınızı giriniz :")
            kitap_iade_et(kutuphane,kullanicilar,kullanici_adi,kitap_ismi)
        elif secim=="5":
            kullanici_adi = input("Kullanıcı adını girin: ")            
            kullanici_bilgileri(kullanicilar,kullanici_adi)
        elif secim=="6":
            print("Kütüphane sisteminden çıkış yapılıyor")
        else :
            print("Hatalı bir seçim yaptınız.")


main()


