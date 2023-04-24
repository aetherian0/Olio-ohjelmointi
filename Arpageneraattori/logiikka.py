class Arpageneraattori:
    def __init__(self):
        pass

    def generoi_arpa(self, id):
        arpa = open(f"Arpageneraattori/arvat/arpa_{id}.txt", "x")
        kirjoita = open(f"Arpageneraattori/arvat/arpa_{id}.txt", "w")
        kirjoita.write("moi")
        kirjoita.close()
        