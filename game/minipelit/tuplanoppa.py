import random

class Tuplanoppa: 
    def __init__(self): 
        '''
        attribuutit
            otsikko : str, luokan nimi
            min, max : int, generoitavan alueen rajat
            noppa1, noppa 2 : int, noppien silmäluvut
        '''
        self.otsikko = "Tuplanoppa" 
        self.min = 0 
        self.max = 6 
        self.noppa1 = random.randint(self.min, self.max)
        self.noppa2 = random.randint(self.min, self.max)
        self.noppa_summa = self.noppa1 + self.noppa2


    def tarkista(self, arvaus): 
        '''
        Tarkistaa onko arvaus oikein suhteessa noppa_summaan.
        Yli, alle tai tasan 7
        '''
        if arvaus == "tasan" and self.noppa_summa == 7 or arvaus == "alle" and self.noppa_summa <= 6 or arvaus == "yli" and self.noppa_summa >= 8:
            return True
        else:
            return False

    def reset(self): 
        '''
        resetoi olion tilan, arpoo uudet noppien silmäluvut
        '''
        self.noppa1 = random.randint(self.min, self.max)
        self.noppa2 = random.randint(self.min, self.max)
        self.noppa_summa = self.noppa1 + self.noppa2

    def tallennus(self): 
        pass

