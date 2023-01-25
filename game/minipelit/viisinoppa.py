import random

class Viisinoppa:  
    def __init__(self):
        '''
        attribuutit
            otsikko : str, luokan nimi
            min, max : int, generoitavan alueen rajat
            nopat : int, noppien silmäluvut
        '''
        self.otsikko = "Viisinoppa"
        self.min = 0
        self.max = 6
        self.noppa1 = random.randint(self.min, self.max)
        self.noppa2 = random.randint(self.min, self.max)
        self.noppa3 = random.randint(self.min, self.max)
        self.noppa4 = random.randint(self.min, self.max)
        self.noppa5 = random.randint(self.min, self.max)
        self.set = {self.noppa1, self.noppa2, self.noppa3, self.noppa4, self.noppa5}
 
 
    def tarkista(self):
        '''
        Tarkistaa onko nopissa samoja silmälukuja
        voitto riippuu montako samaa silmälukua nopista löytyy
        '''
        if len(self.set) == 5:
            return 5
        elif len(self.set) == 4:
            return 4
        elif len(self.set) == 3:
            return 3
        elif len(self.set) == 2:
            return 2
        else:
            return 1    

    def reset(self):
        '''
        resetoi olion tilan, arpoo uudet noppien silmäluvut
        '''
        self.noppa1 = random.randint(self.min, self.max)
        self.noppa2 = random.randint(self.min, self.max)
        self.noppa3 = random.randint(self.min, self.max)
        self.noppa4 = random.randint(self.min, self.max)
        self.noppa5 = random.randint(self.min, self.max)
        self.set = {self.noppa1, self.noppa2, self.noppa3, self.noppa4, self.noppa5}
