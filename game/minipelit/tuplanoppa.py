import random

def main() -> None:

    noppa_summa = random.randint(1, 6) + random.randint(1, 6)   

    f = open("tuplanoppa_pisteet.txt")
    pisteet = str(f.read())
    f.close()

    while True:
        try:
            panos = int(input("Aseta panos: "))
            arvaus = input("Arvaa onko noppien summa tasan, yli vai alle 7: ")

            if arvaus == "tasan":
                print("Arvasit tasan")
                if noppa_summa == 7:
                    print("Arvauksesi on oikein! Noppien summa oli " + str(noppa_summa) + ". " + "Voitit " + str(panos * 1000) + " pistettä!")
                    print("Sinulla on nyt " + pisteet + " pistettä yhteensä.")
                    break
                else:
                    print("Arvauksesi on väärin, noppien summa oli " + str(noppa_summa) + ". Hävisit " + str(panos * 100) + " pistettä.")
                    print("Sinulla on nyt " + pisteet + " pistettä yhteensä.")
                    break

            if arvaus == "alle" or arvaus == "yli":
                print("Arvasit " + arvaus)
                if noppa_summa != 7:
                    print("Arvauksesi on oikein! Noppien summa oli " + str(noppa_summa) + ". " + "Voitit " + str(panos * 100) + " pistettä!")
                    print("Sinulla on nyt " + pisteet + " pistettä yhteensä.")
                    break
                else:
                    print("Arvauksesi on väärin, noppien oli " + str(noppa_summa) + ". Hävisit " + str(panos * 10) + " pistettä.")
                    print("Sinulla on nyt " + pisteet + " pistettä yhteensä.")
                    break

        except:
            print("Tarkista syötteesi!")
            continue


if __name__=='__main__':
    main()