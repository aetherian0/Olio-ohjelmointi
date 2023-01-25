import random

class Tuplanoppa: 
    def __init__(self): 
        self.otsikko = "TuplaNoppa" 
        self.min = 0 
        self.max = 6 
        self.noppa1 = 0 
        self.noppa2 = 0 


    def tarkista(self, parameter): 
        return False 

    def reset(self): 
        raise NotImplementedError 

    def tallennus(self): 
        raise NotImplementedError 

