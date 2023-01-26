import random
from datetime import datetime

class Tänäänon:
    def __init__(self):
        '''
        attribuutit
            otsikko : str, luokan nimi ja kuvaava ohje
            viikonpäivät : list, lista kaikista viikonpäivistä
            päiväys : date, kokonainen päivämäärä numeroina
            päivä_numerona : int, monesko päivä viikosta numerona
            tänään : str, päivän nimi kirjaimina
            arvausten_määrä : int, arvausten määrä
        '''
        self.otsikko = "Tänään on"
        self.viikonpäivät = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.päiväys = datetime.now()
        self.päivä_numerona = Päivämäärä.weekday()
        self.tänään = self.päiväys.strftime("%A")
        self.arvausten_määrä = 0
        
   
    def tarkista(self, arvaus):
        '''
        Tarkistaa onko arvattu viikonpäivä oikea sekä kasvattaa arvausten määrää yhdellä
        '''
        self.arvausten_määrä += 1
        return arvaus == self.tänään

    def reset(self):
        pass	

    def tallennus(self):
        pass



# Kertoo päivämäärän
Päivämäärä = datetime.now()

# Kertoo päivän numerona 0-6
päivä = Päivämäärä.weekday()

#Kertoo viikonpäivän
viikon_päivät=["Maanantai", "Tiistai", "Keskiviikko","Torstai","Perjantai","Lauantai","Sunnuntai"]
viikon_päivät1=["Maanantai", "Tiistai", "Keskiviikko","Torstai","Perjantai","Lauantai","Sunnuntai"]
viikon_päivät1.remove(viikon_päivät1[päivä])
#print(viikon_päivät)


#print(viikon_päivät[päivä])

Random=random.sample(viikon_päivät1, 3)
lista1 = str(Random)
lista1 = lista1.replace("[","")
lista1 = lista1.replace("]","")
lista2 = str(viikon_päivät[päivä])

print(lista1 + ", " + "'" + lista2 + "'")
