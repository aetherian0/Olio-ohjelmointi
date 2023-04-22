import tkinter as tk
import tkinter.ttk as ttk

from logiikka import Arpageneraattori


class Ikkuna(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Arpageneraattori")
        self.geometry("300x200+600+200")
        self.configure(background = "pink")

        self.ohje1 = tk.Label(self, text = "Anna generoitavien arpojen määrä")
        self.ohje1.grid(column = 0, row = 0)

        self.arpojen_maara = tk.Entry(self)
        self.arpojen_maara.grid(column = 0, row = 1)

        # tyhjä rivi
        self.tyhja1 = tk.Label(self, text = "\n")
        self.tyhja1.grid(column = 0, row = 2)

        self.ohje2 = tk.Label(self, text = "Anna todennäköisyys millä 1 arpa voittaa")
        self.ohje2.grid(column = 0, row = 3)

        self.todennakoisuus = tk.Entry(self)
        self.todennakoisuus.grid(column = 0, row = 4)

        # tyhjä rivi
        self.tyhja2 = tk.Label(self, text = "\n")
        self.tyhja2.grid(column = 0, row = 5)

        # nappi joka generoi arvat
        self.nappi = tk.Button(self, text = "Generoi")
        self.nappi.grid(column = 0, row = 6)

        


if __name__ == "__main__":
    Ikkuna().mainloop()
