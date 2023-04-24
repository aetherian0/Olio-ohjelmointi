import random

class Arpageneraattori:
    def __init__(self):
        pass

    def generoi_arpa(self, id, voitto_prosentti):
        
        random_luku = round(random.random() * 100)
        arpa = open(f"Arpageneraattori/arvat/arpa_{id}.txt", "x")
        kirjoita = open(f"Arpageneraattori/arvat/arpa_{id}.txt", "w")

        if int(random_luku) < int(voitto_prosentti):
            kirjoita.write("voitto!")
        else:
            kirjoita.write("Ei voittoa!")

        kirjoita.close()
        