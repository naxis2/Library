library = []
def kitap_ekle(adi, yazar, yil):
    kitap = {
        "ad": adi,
        "yazar": yazar,
        "yil": yil
    }
    library.append(kitap)
    print(f"'{adi}' adlı kitap kütüphaneye eklendi.")

def kitap_sil(index):
    if 0 <= index < len(library):
        silinen = library.pop(index)
        print(f"'{silinen['ad']}' adlı kitap kütüphaneden silindi.")
    else:
        print("Geçersiz indeks!")

def kitaplari_goster():
    if library:
        print("\nKütüphanedeki kitaplar:")
        for i, kitap in enumerate(library, 1):
            print(f"{i}. {kitap['ad']} - {kitap['yazar']} ({kitap['yil']})")
    else:
        print("Kütüphane boş.")

while True:
    print("\n--- Kütüphane Menüsü ---")
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitapları Göster")
    print("4. Çıkış")

    secim = input("Seçiminizi yapın (1-4): ")

    if secim == "1":
        ad = input("Kitap adı: ")
        yazar = input("Yazar: ")
        yil = input("Yayın yılı: ")
        kitap_ekle(ad, yazar, yil)

    elif secim == "2":
        kitaplari_goster()
        try:
            index = int(input("Silmek istediğiniz kitabın numarası: ")) - 1
            kitap_sil(index)
        except ValueError:
            print("Lütfen sayı girin!")

    elif secim == "3":
        kitaplari_goster()

    elif secim == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.")
