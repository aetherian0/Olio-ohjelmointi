# -*- coding: utf-8 -*-
'''
Konsoliohjelma minipelikokoelmanlle (proceduraalista ohjelmointia=
Jokainen minipeli on oma luokkansa.
minipelien tuonti (import) ei saa aiheuttaa sivuvaikutuksia.
Hoitaa kaiken käyttäjän ja pelien välisen vuorovaikutuksen. 
'''
import tkinter as tk
import tkinter.ttk as ttk
import math
import os 
import minipelit
import datetime
from minipelit.arvaaluku import ArvaaLuku
from minipelit.tuplanoppa import Tuplanoppa
from minipelit.viisinoppa import Viisinoppa
from minipelit.tanaanonpeli import Tanaanonpeli


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minipelikokoelma")
        self.geometry("700x400+610+200")  
        self.configure(background="grey")

        # Sulkee kaikki ohjelmat esc-näppäintä painaessa
        self.bind("<Escape>", self._sulje)     


        # Laatikot pelien nimille
        self.tanaanon = ttk.Button(self, text = "Tänään on", command = self.avaa_tanaanon)
        self.tanaanon.grid(row = 1, padx = 300, pady = (45, 25))
        self.tanaanon.config(width = 15)

        self.arvaaluku = ttk.Button(self, text = "Arvaa luku", command = self.avaa_arvaaluku)
        self.arvaaluku.grid(row = 2, padx = 10, pady = 25)
        self.arvaaluku.config(width = 15)

        self.viisinoppa = ttk.Button(self, text = "Viisinoppa", command = self.avaa_viisinoppa)
        self.viisinoppa.grid(row = 3, padx = 10, pady = 25)
        self.viisinoppa.config(width = 15)

        self.tuplanoppa = ttk.Button(self, text = "Tuplanoppa", command = self.avaa_tuplanoppa)
        self.tuplanoppa.grid(row = 4, padx = 10, pady = 25)
        self.tuplanoppa.config(width = 15)

        self.avaa_viimeisin()

    def avaa_tanaanon(self):

        # tallentaa pelin peli.conf tiedostoon
        pelin_tila = open("peli.conf", "w")
        pelin_tila.write("tanaanon")

        # Tarkistetaan onko peliä pelattu jo tänään
        tiedosto = open("date.txt", "r")
        z = tiedosto.readline()
        x = datetime.datetime.today()
        y = x.strftime("%Y-%m-%d")
        if z == y:
            ilmoitus = tk.Toplevel()
            ilmoitus.geometry("400x75")
            ilmoitus.configure(background = "grey")
            pelin_nimi = self.tanaanon["text"]
            ilmoitus.title(pelin_nimi)
            virhe = ttk.Label(ilmoitus, font = ("calibri", 20), text = "Olet pelannut tätä peliä jo tänään!")
            virhe.grid(column = 0, row = 0)
            tiedosto.close()
        else:    
            tiedosto = open("date.txt", "w")
            tänään = datetime.date.today()
            tiedosto.write(str(tänään))
            tiedosto.close()

            # Luo uuden ikkunan ja määritetään peli
            uusi = tk.Toplevel()
            peli = Tanaanonpeli()
            pelin_nimi = self.tanaanon["text"]
            uusi.title(pelin_nimi)
            uusi.geometry("700x400")
            kysymys = ttk.Label(uusi, text = "Mikä päivä tänään on?")
            kysymys.grid(column = 0, row = 0)
            uusi.configure(background="grey")


    def avaa_arvaaluku(self):

        # tallentaa pelin peli.conf tiedostoon
        pelin_tila = open("peli.conf", "w")
        pelin_tila.write("arvaaluku")

        # Luo uuden ikkunan
        uusi = tk.Toplevel()
        peli = ArvaaLuku()
        pelin_nimi = self.arvaaluku["text"]
        uusi.title(pelin_nimi)
        uusi.geometry("700x400")
        kysymys = ttk.Label(uusi, text = "Arvaa luku 1 ja 10 väliltä")
        kysymys.grid(column = 0, row = 0)
        uusi.configure(background="grey")


    def avaa_viisinoppa(self):

        # tallentaa pelin peli.conf tiedostoon
        pelin_tila = open("peli.conf", "w")
        pelin_tila.write("viisinoppa")

        # Luo uuden ikkunan
        peli = Viisinoppa()
        uusi = tk.Toplevel()
        pelin_nimi = self.viisinoppa["text"]
        uusi.title(pelin_nimi)
        uusi.geometry("700x400")
        kysymys = ttk.Label(uusi, text = "Arvaa montako paria noppien heitosta tuli")
        kysymys.grid(column = 0, row = 0)
        uusi.configure(background="grey")


    def avaa_tuplanoppa(self):

        # tallentaa pelin peli.conf tiedostoon
        pelin_tila = open("peli.conf", "w")
        pelin_tila.write("tuplanoppa")

        # Luo uuden ikkunan
        uusi = tk.Toplevel()

        # Tuplanoppa pitää kirjoittaa uusiksi, koska aikaisempi ryhmä on kirjoittanut sen niin että luokka kutsuu inputin kun
        # luokka kutsutaan, tämä mekaniikka pitää poistaa, jotta peli on mahdollista tehdä toimivaksi
        #peli = Tuplanoppa()
        pelin_nimi = self.tuplanoppa["text"]
        uusi.title(pelin_nimi)
        uusi.geometry("700x400")
        kysymys = ttk.Label(uusi, text = "Arvaa onko noppien summa alle, tasan vai yli 7")
        kysymys.grid(column = 0, row = 0)
        uusi.configure(background="grey")
        arvaus = ttk.Entry(uusi)
        arvaus.grid(column = 0, row = 1)


    # Avaa viimeiseksi avattu peli kun ohjelma käynnistetään 
    def avaa_viimeisin(self):
        peli_on = open("peli.conf", "r")

        match peli_on.readline():
            case "tanaanon":
                self.avaa_tanaanon()
            
            case "arvaaluku":
                self.avaa_arvaaluku()

            case "viisinoppa":
                self.avaa_viisinoppa()

            case "tuplanoppa":
                self.avaa_tuplanoppa()


    # Sulkee kaikki ikkunat
    def _sulje(self, e):
        self.destroy()


    def pelaa(self, peli) -> None:
        '''
        driveri parametrina saadulle pelille 
        '''
        #  testi peli käyttää ArvaaLuku luokkaa
        if peli.otsikko == ' Arvaa luku väliltä 1..9 ':
            while True:
                try:
                    if peli.lukuja == 1: #  arvaa kunnes käyttäjä ei enää halua uutta peliä
                        arvaus = int(input(peli.otsikko))
                        if peli.tarkista(arvaus):
                            print(f"{', '.join(map(str, peli.magic))} on oikein, vain ", \
                                f"{len(peli.arvaukset['oikein'])+len(peli.arvaukset['väärin'])} arvausta!")
                            if not self.uudestaan(peli):
                                break
                            else:
                                continue
                        else:
                            print('Liian korkea! ' if arvaus > peli.magic[0] else 'Liian matala!')
                            continue

                except Exception as e:
                    print('Check your input, only integers are allowed', e)

        #  Tuplanoppa peli
        elif peli.otsikko == "Tuplanoppa":
            while True:
                try:
                    print("Sinun pitää arvata, onko kahden nopan summa alle, tasan vai yli 7! Onnea matkaan!")
                    
                    arvaus = int(input("Arvaa summa (2-12): "))

                    if peli.tarkista(arvaus):
                        print(f"Heitetyt luvut olivat { peli.heitto1,peli.heitto2 } ja niiden summa: {peli.sum}")
                        print(f"Onneksi olkoon! Voitit juuri {peli.voitto} pistettä!")

                    else:
                        print(f"Heitetyt luvut olivat { peli.heitto1,peli.heitto2 } ja niiden summa: {peli.sum}", \
                            f"Voi ei! Hävisit juuri {peli.havio} pistettä!")
                    if not self.uudestaan(peli):
                        break
                    else:
                        continue
                except:
                    print("OOPS, tarkista syötteesi!")
                    
        #  Viisinoppa peli     
        elif peli.otsikko == "Viisinoppa":
            while True:
                try:
                    panos = int(input("Mikä on panoksesi?: "))
                    if peli.tarkistus(panos) == True:
                        print("Heitetään ensiksi nopat", peli.heitot)
                        print("Voitit!", peli.tulos)
                    else:
                        print("Heitetään ensiksi nopat", peli.heitot)
                        print("Ei voittoa")
                    if not self.uudestaan(peli):
                        break
                    else:
                        continue

                except:
                    print("OOPS, tarkista syötteesi!")
                """
                try:
                    if peli.panos >= peli.min and peli.panos <= peli.max:
                        break
                    else:
                        print("Anna luku 1-100 väliltä.")

                except ValueError as r:
                        print("Vain numerot käyvät.", r)
                """


        elif peli.otsikko == "Tänään on -peli":
            while True:
                try:
                    if peli.tarkistus(input("Mikä päivä tänään on?:")) == True:
                        print("Oikein! Tänään on " + str(peli.viikko[peli.paiva]) + ".")
                        break
                    else:
                        print("Väärin, tässä vihje: Eilen oli " + str(peli.viikko[peli.vihje()]) + ".")
                except:
                    print("OOPS, tarkista syötteesi!")


    # Double checkkaa jos tätä edes tarvitaan sitten kun peli on valmis, samaa kuin menu alla
    def uudestaan(self, peli):
        '''
        aloittaa pelin uudelleen kutsumalla sen reset-metodia

        Parametrit
            peli: yksi minipeleistä

        Return
            True, jos pelaaja haluaa pelata uudelleen
            
        '''
        
        if input('Uusi peli? [K|E] ').upper() == 'K':
            peli.reset()
            clear()
            return True
        else:
            return False

    # POISTA MENU FUNKTIO SITTEN KUN PELIÄ ON KOKONAAN VALMIS, TÄTÄ EI TARVITA JOS PELIÄ EI PELATA TERMINAALISSA!
    def menu(self):

        '''
        Ohjelman käynnistyessä tulostaa valikon minipeleistä.
        Peli valitaan ja aloitetaan syöttämällä sitä vastaava numero.
        '''
        
        peli = None
        
        while True:
            clear()
            print('''
            Minipelikokoelma:
                
            1. Tänään on
            2. Viisinoppa
            3. Tuplanoppa
            4. Testipeli: Arvaa luku
            5. Lopeta
            ''')
            valinta = ''
            while valinta not in ('1', '2', '3', '4'):
                valinta = input('\tValinta: ')
                break
            match valinta: #3.10 or newer
                case '1':
                #  peli = # lisää oma peli oliosi
                    print('Peli 1 valittu')
                    peli = Tanaanonpeli()
                case '2':
                # peli = # lisää oma peli oliosi
                    print('Peli 2 valittu')
                    peli = Viisinoppa()
                case '3':
                # peli = # lisää oma peli oliosi
                    print('Peli 3 valittu')
                    peli = Tuplanoppa()
                case '4':
                    peli = ArvaaLuku(str(' Arvaa luku väliltä 1..9 '), range(1, 9), int(1))
                case _:
                    break

            if peli:
                self.pelaa(peli) #  pelaa kunnes peli on valmis ja käyttäjä ei halua uutta peliä
                peli = None #  pelaaja voi valita uuden pelin tai lopettaa


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Windowsissa cls
        command = 'cls'
    os.system(command)
        

if __name__ == '__main__':
    App().mainloop()