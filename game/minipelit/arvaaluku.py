import random

class ArvaaLuku:
    '''
    ArvaaLuku tietää satunnaisesti generoidun luvun magic väliltä min..max
    ja osaa tarkistaa onko annettu luku sama kuin magic ja osaa
    resetoida tilansa
    '''
    def __init__(self):
        '''
        attribuutit
            otsikko : str, luokan nimi ja kuvaava ohje
            min, max : int, generoitavan alueen rajat
            magic : int, satunasiesti generoitu luku
            arvaukset : int, arvausten määrä
        '''
           
        self.otsikko = "Arvaa luku"
        self.min = 1
        self.max = 9
        self.magic = random.randint(self.min, self.max)
        self.arvaukset = 0


    def tarkista(self, arvaus):
        '''
        Tarkistaa onko annettu luku sama kuin magic ja päivittää arvaukset

        parametrit
            arvaus:int, tarkistettava luku

        return
            bool: True = arvaus == magic number
        '''

        self.arvaukset += 1
        return arvaus == self.magic


    def reset(self):
        '''
        resetoi olion tilan 
        '''

        self.magic = random.randint(self.min, self.max)
        self.arvaukset = 0
