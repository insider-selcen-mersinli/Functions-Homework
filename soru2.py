def sayi_atama(sayi):
    x = sayi
    print("1.Yol -> " + sayi_okunusu(x))
    print("2.Yol -> " + sayi_okunusu2(x))


def sayi_okunusu(sayi):
    onlar_basamagi_array = [[10, "on"], [20, "yirmi"], [30, "otuz"], [40, "kirk"], [50, "elli"], [60, "altmis"],
                            [70, "yetmis"], [80, "seksen"], [90, "doksan"]]
    birler_basamagi_array = [[0, ""], [1, "bir"], [2, "iki"], [3, "uc"], [4, "dort"], [5, "bes"], [6, "alti"],
                             [7, "yedi"], [8, "sekiz"], [9, "dokuz"]]

    birler_basamagi = sayi % 10
    onlar_basamagi = sayi // 10

    sayi_string = ""
    for x in range(0, 9):
        if onlar_basamagi_array[x][0] == (onlar_basamagi * 10):
            sayi_string += onlar_basamagi_array[x][1] + " "
            break

    for y in range(0, 9):
        if birler_basamagi_array[y][0] == birler_basamagi:
            sayi_string += birler_basamagi_array[y][1]
            break

    return sayi_string


def sayi_okunusu2(sayi):
    onlar_basamagi_array = ["", "on", "yirmi", "otuz", "kirk", "elli", "altmis", "yetmis", "seksen", "doksan"]
    birler_basamagi_array = ["", "bir", "iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"]

    birler_basamagi = sayi % 10
    onlar_basamagi = sayi // 10

    sayi_string = ""
    for x in range(0, 9):
        if x == onlar_basamagi:
            sayi_string += onlar_basamagi_array[x] + " "
            break

    for y in range(0, 9):
        if y == birler_basamagi:
            sayi_string += birler_basamagi_array[y]
            break

    return sayi_string


sayi = int(input("Okunusunu ogrenmek istediginiz iki basamakli sayiyi giriniz: "))
sayi_atama(sayi)
