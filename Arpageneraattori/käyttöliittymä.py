import tkinter as tk
import random
import os

from logiikka import Arpageneraattori


class Ikkuna(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Arpageneraattori")
        self.geometry("400x200+600+200")
        self.configure(background = "pink")

        self.ohje1 = tk.Label(self, text = "Anna generoitavien arpojen määrä")
        self.ohje1.grid(column = 0, row = 0)

        self.arpojen_maara = tk.Entry(self)
        self.arpojen_maara.grid(column = 0, row = 1)

        # tyhjä rivi
        self.tyhja1 = tk.Label(self, text = "\n")
        self.tyhja1.grid(column = 0, row = 2)

        self.ohje2 = tk.Label(self, text = "Anna todennäköisyys jolla yksittäinen arpa voittaa väliltä 0-100%")
        self.ohje2.grid(column = 0, row = 3)

        self.todennakoisuus = tk.Entry(self)
        self.todennakoisuus.grid(column = 0, row = 4)

        # tyhjä rivi
        self.tyhja2 = tk.Label(self, text = "\n")
        self.tyhja2.grid(column = 0, row = 5)

        # nappi joka generoi arvat
        self.nappi = tk.Button(self, text = "Generoi", command = self.generoi)
        self.nappi.grid(column = 0, row = 6)
    

    def generoi(self):
        # Koodi pyöritetään vain jos molempii entryihin on kirjoittu jotain ja todennäköisyyden tulee olla 0 ja 100 välillä
        if len(self.arpojen_maara.get()) > 0 and len(self.todennakoisuus.get()) > 0 and int(self.todennakoisuus.get()) < 101 and int(self.todennakoisuus.get()) > -1:

            arpa_generaattori = Arpageneraattori()

            for i in range(int(self.arpojen_maara.get())):
                # Jokaisen arvan ID arvotaan 10 miljoonan ja 99 miljoonan väliltä random luvuksi
                arpa_generaattori.generoi_arpa(random.randint(10000000, 99999999), self.todennakoisuus.get())


            arvat_path = os.path.abspath(os.path.join(os.getcwd(), "Arpageneraattori", "arvat"))
            os.startfile(arvat_path)

        
def main():
    Ikkuna().mainloop()

if __name__ == "__main__":
    main()
