import random
from datetime import datetime

class Tänäänon:
    def __init__(self):
        '''
        attribuutit
            otsikko : str, luokan nimi ja kuvaava ohje
            viikonpäivät : list, lista kaikista viikonpäivistä
            tänään : str, päivän nimi kirjaimina
            arvausten_määrä : int, arvausten määrä
            randompäivä1 : 2, 3: str, arvottu päivä
            lista : str, lista mikä sisältää oikean päivän ja kolme arvottua päivää
            status : str, merkintä siitä monennellako arvauksella pelaaja arvasi oikein
        '''
        self.otsikko = "Tänään on"
        self.viikonpäivät = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.tänään = datetime.now().strftime("%A")
        self.arvausten_määrä = 0
        self.status = ""

        # Poistaa tämän hetkisen päivän viikonpäivät listasta
        self.viikonpäivät.remove(self.tänään)

        # Sekoittaa jäljellä olevat päivät viikonpäivät listassa
        random.shuffle(self.viikonpäivät)

        self.randompäivä1 = self.viikonpäivät[0]
        self.randompäivä2 = self.viikonpäivät[1]
        self.randompäivä3 = self.viikonpäivät[2]

        self.lista = [self.tänään, self.randompäivä1, self.randompäivä2, self.randompäivä3]
        
   
    def tarkista(self, arvaus):
        '''
        Tarkistaa onko arvattu viikonpäivä oikea sekä kasvattaa arvausten määrää yhdellä
        '''
        self.arvausten_määrä += 1
        return arvaus == self.tänään

    def tallennus(self):
        pass
