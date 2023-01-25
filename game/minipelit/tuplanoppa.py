class TuplaNoppa: 
    def __init__(self): 
        self.otsikko = "" 
        self.min = 0 
        self.max = 0 
        self.noppa1 = 0 
        self.noppa2 = 0 


    def tarkista(self, parameter): 
        return False 


    def reset(self): 
        raise NotImplementedError 

    def tallennus(self): 
        raise NotImplementedError 

