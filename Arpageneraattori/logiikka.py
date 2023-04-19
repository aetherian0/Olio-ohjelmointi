import time

class Arpageneraattori:
    def __init__(self):
        self.id = round(time.time())

    def generoi_arpa(self):

        # keksi parempi tapa tähän
        arpa = open("Arpageneraattori/arvat/arpa_" + str(self.id) + ".txt" ,"x")
        