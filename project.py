

import random

words = ["armut", "çilek", "kiraz", "kavun"]
tahmin = ""
kalan_hak = 5
kalan_hak_bitis = False
dogru_sayisi = 0 

name = input("Adin nedir?")
print("Bol Sans!", name, ",", "bu bir 5 harfli meyve.")

word = random.choice(words)
print(word)

while tahmin != words and not(kalan_hak_bitis):

    tahmin = input("Bir harf tahmininde bulun:")
    print(tahmin)

    if tahmin in word:
        print("doğru")
        dogru_sayisi += 1
    else:
        print("yanlis")
        kalan_hak -= 1

    print(kalan_hak)

    if kalan_hak == 0:
        kalan_hak_bitis=True
        print("Kaybettiniz!")
    if dogru_sayisi == 5:
        print("Kazandiniz!")
        break

print(word)





   
