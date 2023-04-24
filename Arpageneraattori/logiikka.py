import random

class Arpageneraattori:
    def __init__(self):
        pass

    def generoi_arpa(self, id, voitto_prosentti):

        random_luku = round(random.random() * 100)
        arpa = open(f"Arpageneraattori/arvat/arpa_{id}.txt", "x")
        kirjoita = open(f"Arpageneraattori/arvat/arpa_{id}.txt", "w")

        # Jos käyttäjä kirjoittama voittoprosentti on suurempiu kuin arvottu luku väliltä 0-100 niin arpaan kirjoitetaan "voitto!"
        if int(random_luku) < int(voitto_prosentti):
            tulos = "Voitto"
            kirjoita.write("voitto!")
        else:
            tulos = "Ei voittoa"
            kirjoita.write("Ei voittoa!")

        kirjoita.close()

        # Yksittäinen arpa lisätään "kaikki arvat.txt" tiedostoon, josta näkee arvan ID:n sekä voittiko arpa
        arkisto = open("Arpageneraattori/kaikki arvat.txt", "a")
        arkisto.write(str(id) + ", " + tulos + "\n")
        arkisto.close()
        