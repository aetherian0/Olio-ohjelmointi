from datetime import datetime
import random

"""
Tänään on peli (alunperin Inkan vastuulla, hän ei saanut tehtyä koodia)
Uuden koodin kirjoittanut Arttu
Valitsee satunnaisen viikonpäivän, joka täytyy arvata.
Uudemman version tarvitsee näyttää neljä viikonpäivää, joista yksi on todellinen.
"""

class Tanaanonpeli:
    """
    Kysyy pelaajalta viikonpäivän
    Toimii hakemalla viikonpäivän numeron 0-6, missä 0 on maanantai
    Valitsee viikonpäivän nimen viikonpäivän numeron avulla
    Pyytää käyttäjään syöttämään viikonpäivän nimen, ja tarkistaa onko vastaus oikein
    Jos vastaus on väärin, kertoo eilisen viikonpäivän
    """

    def __init__(self):
        self.otsikko = "Tänään on -peli"
        self.viikko = ["maanantai","tiistai","keskiviikko","torstai","perjantai","lauantai","sunnuntai"]
        self.dt = datetime.now()
        self.__paiva = self.dt.weekday()


    @property
    def paiva(self):
        return self.__paiva

    @paiva.setter
    def paiva(self, value):
        raise ValueError("Päivä on vain luettavissa")


    #tarkistaa käyttäjän valinnan
    def tarkistus(self, valinta):
        if valinta == self.viikko[self.__paiva]:
            return True
        else:
            return False


    #kertoo vihjeenä eilisen päivän
    def vihje(self):
        if self.__paiva != 0:
            return (self.__paiva - 1)
        else:
            return 6


    #resetoi pelin
    def reset(self):
        self.__paiva = self.dt.weekday()
