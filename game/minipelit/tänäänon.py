import random

from datetime import datetime

class TänäänOn:
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
lista1= str(Random)
lista1=lista1.replace("[","")
lista1=lista1.replace("]","")
lista2 = str(viikon_päivät[päivä])

print(lista1+", "+ "'"+lista2+"'")
