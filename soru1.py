def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):
    tam_bolunenler = []
    for x in range(min_sayi, max_sayi):
        sonuc = x % bolen_sayi
        if sonuc == 0:
            tam_bolunenler.append(x)

    print("Tam bolunen degerler -> ", tam_bolunenler)
    return len(tam_bolunenler)


print("Bu kodun görevi verilen deger araliklarinda belirttiğiniz sayiya tam bolunen sayilari size gostermektir.")
min_sayi = int(input("Deger araligi için min sayiyi giriniz: "))
max_sayi = int(input("Deger araligi için max sayiyi giriniz: "))
bolen_sayi = int(input("Bu araliktaki degerlerin hangi sayiya tam bolunmesini istediginizi giriniz: "))
print(bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi), "tane sayi", bolen_sayi, "sayisina tam bolunuyor")
