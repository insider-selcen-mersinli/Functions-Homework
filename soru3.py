def harf_notu(vize1, vize2, final):
    ders_notu = ((vize1 / 100) * 30) + ((vize2 / 100) * 30) + ((final / 100) * 40)

    if ders_notu >= 90:
        print("AA")
    elif ders_notu >= 85:
        print("BA")
    elif ders_notu >= 80:
        print("BB")
    elif ders_notu >= 75:
        print("CB")
    elif ders_notu >= 70:
        print("CC")
    elif ders_notu >= 65:
        print("DC")
    elif ders_notu >= 60:
        print("DD")
    elif ders_notu >= 55:
        print("FD")
    else:
        print("FF")


vize_1 = input("1.vize notunu giriniz: ")
vize_2 = input("2.vize notunu giriniz: ")
final = input("Final notunu giriniz: ")
harf_notu(int(vize_1), int(vize_2), int(final))
