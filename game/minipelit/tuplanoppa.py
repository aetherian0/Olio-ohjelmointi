import random

def main() -> None:

    noppa_summa = random.randint(1, 6) + random.randint(1, 6)

    while True:
        try:
            panos = int(input("Aseta panos: "))
            arvaus = input("Arvaa onko noppien summa alle, yli vai tasan 7: ")

            if arvaus == "tasan":
                print("Arvasit tasan")
                if noppa_summa == 7:
                    print("Vastauksesi on oikein! Voitit " + str(panos * 1000) + " pistettä!")
                    break
                else:
                    print("Vastauksesi on väärin, oikea vastaus oli " + str(noppa_summa) + ". Hävisit " + str(panos * 100) + " pistettä.")

            if arvaus == "alle" or arvaus == "yli":
                print("Arvasit yli tai alle")
                if noppa_summa != 7:
                    print("Vastauksesi on oikein! Voitit " + str(panos * 100) + " pistettä!")
                    break
                else:
                    print("Vastauksesi on väärin, oikea vastaus oli " + str(noppa_summa) + ". Hävisit " + str(panos * 10) + " pistettä.")

        except:
            print("Tarkista syötteesi!")
            continue

if __name__=='__main__':
    main()