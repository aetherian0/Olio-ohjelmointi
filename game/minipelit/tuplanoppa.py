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
        self.noppa1 = random.randint(min, max)
        self.noppa2 = random.randint(min, max)


    def tarkista(self, arvaus): 
        return False 

    def reset(self): 
        raise NotImplementedError 

    def tallennus(self): 
        pass

