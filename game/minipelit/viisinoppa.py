import random

class Viisinoppa:  
    def __init__(self):
        '''
        attribuutit
            otsikko : str, 
            min, max : int, 
            nopat : int, 
        '''
        self.otsikko = "Viisinoppa"
        self.min = 0
        self.max = 6
        self.noppa1 = random.randint(self.min, self.max)
        self.noppa2 = random.randint(self.min, self.max)
        self.noppa3 = random.randint(self.min, self.max)
        self.noppa4 = random.randint(self.min, self.max)
        self.noppa5 = random.randint(self.min, self.max)
 
 
    def tarkista(self):
        return 0

    def reset(self):
        raise NotImplementedError
