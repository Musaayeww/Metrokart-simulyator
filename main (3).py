# METROKART SIMULYATORU

pin = "1234"
cehd = 0

balans = 0
borc = 0
gedis = 0
limit = 100
gunluk_artirma = 0

emeliyyatlar = []

# PIN giris
while cehd < 3:
    daxil = input("PIN daxil et: ")

    if daxil == pin:
        print("Giris ugurludur")
        break
    else:
        cehd += 1
        print("Sehv PIN")

if cehd == 3:
    print("Proqram dayandi")

else:

    while True:

        print("\n1 Balansi goster")
        print("2 Balans artir")
        print("3 Gedis et")
        print("4 Son emeliyyatlar")
        print("5 Gunluk statistika")
        print("6 Parametrler")
        print("0 Cixis")

        secim = input("Secim: ")

        # BALANS GOSTER
        if secim == "1":
            print("Balans:", balans)
            print("Borc:", borc)

        # BALANS ARTIR
        elif secim == "2":

            mebleg = float(input("Mebleg daxil et: "))

            if mebleg <= 0:
                print("Sehv mebleg")

            elif gunluk_artirma + mebleg > limit:
                print("Gunluk limit kecildi")

            else:

                gunluk_artirma += mebleg

                if borc > 0:
                    if mebleg >= borc:
                        mebleg -= borc
                        borc = 0
                    else:
                        borc -= mebleg
                        mebleg = 0

                balans += mebleg
                emeliyyatlar.append("Balans artirildi")

        # GEDIS
        elif secim == "3":

            if gedis == 0:
                qiymet = 0.40
            elif gedis <= 3:
                qiymet = 0.36
            else:
                qiymet = 0.30

            if balans >= qiymet:
                balans -= qiymet
                gedis += 1
                emeliyyatlar.append("Gedis edildi")
                print("Turniket kecildi")

            elif 0.30 <= balans < 0.40:
                print("Tecili kecid edildi")
                balans = 0
                borc += 0.10
                gedis += 1

            else:
                print("Balans kifayet deyil")

        # SON EMELIYYATLAR
        elif secim == "4":

            n = int(input("Nece emeliyyat gosterilsin: "))

            for i in emeliyyatlar[-n:]:
                print(i)

        # STATISTIKA
        elif secim == "5":

            print("Gedis sayi:", gedis)
            print("Gunluk artirma:", gunluk_artirma)

        # PARAMETRLER
        elif secim == "6":

            print("1 Limit deyis")
            sec = input("Secim: ")

            if sec == "1":
                limit = float(input("Yeni limit: "))
                print("Limit deyisdi")

        # CIXIS
        elif secim == "0":
            print("Proqram bitdi")
            break

        else:
            print("Yanlis secim")
