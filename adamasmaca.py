from random import randint

kelimeler = [
        "Python", "Bilgisayar", "Programlama", "Veri", "Fonksiyon", "Liste",
        "Sözlük", "Modül", "Dosya", "String", "Sayı", "Matematik", "Döngü",
        "Koşul", "Değişken", "Öğe", "Kütüphane", "Oyun", "İşlemci", "Bellek",
        "Algoritma", "Arama", "Sıralama", "Karar", "Yığın", "Kuyruk",
        "Veritabanı", "Web", "Ağ", "Nesne", "Sınıf", "Metot", "Arayüz",
        "Kapsülleme", "Miras", "Çok biçimlilik", "Soyutlama", "Veri yapısı",
        "Ağaç", "Graf", "Bağlı liste", "Pil", "Klavye", "Ekran", "Fare",
        "Kamera", "Sensör", "Hoparlör", "Mikrofon", "İnternet", "Sunucu",
        "Müzik", "Resim", "Video", "Bilim", "Matematik", "Fizik", "Kimya",
        "Biyoloji", "Mühendislik", "Robot", "Uzay", "Gezegen", "Galaksi",
        "Evren", "Gezegenler", "Yıldız", "Aydınlatma", "Elektrik", "Mıknatıs",
        "Buhar", "Hız", "Enerji", "Rüzgar", "Güneş", "Hidroelektrik",
        "Lisans", "Doktora", "Üniversite", "Okul", "Öğrenci", "Öğretmen",
        "Kitap", "Kalem", "Defter", "Bilgisayar oyunu", "Masaüstü",
        "Dizüstü", "Tablet", "Cep telefonu", "Yapay zeka", "Kriptografi",
        "Kuantum", "Yenilenebilir enerji", "Biyomedikal", "Uzaktan eğitim",
        "Siber güvenlik", "Yapay organ", "Bulut bilişim", "Uzay mekiği",
        "Sanal gerçeklik", "Artırılmış gerçeklik", "Yapay et", "Hologram"
    ]

def verialma(guess):
	if len(guess) == 1:
		return True
	else:
		return False

name = input("isminiz : ")
while True:
	print(f"Merhaba {name} adam asmaca oyununa hoşgeldin!!")
	guess_str = ""
	rastgele = randint(0,len(kelimeler))
	player_1_secret_word = kelimeler[rastgele].upper()
	lives = 10
	while lives > 0:
		character_left = 0
		kelime = []

		for character in player_1_secret_word:
			if character in guess_str:
				kelime.append(character)
			elif character == " ":
				kelime.append(character)
			else:
				kelime.append("_")
				character_left += 1

		print(*kelime)

		if character_left == 0 :
			print("KAZANDIN !!!") 
			break
		
		guess = input("Bir harf tahminde bulununuz : ")
		guess = guess.upper()
		result = verialma(guess)

		if result == True:
			guess_str += guess 
			if guess not in player_1_secret_word:
				lives -= 1
				print("Yanlış tahmin !!!")
				print(f"Canınız {lives} kalmıştır!!!")

				if lives == 0:
					print("Öldün")
					print("Kelime : "+player_1_secret_word.capitalize())
				pass
				
		else:
			print("Lütfen 1 harf gir lan")
			pass

	

