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
        # Kaikki nopat ovat eri, settiin jää 5 eri lukua
        if len(self.set) == 5:
            return 1
        # 2 nopista on samoja, settiin jää 4 eri lukua
        elif len(self.set) == 4:
            return 2
        # 3 nopista on samoja, settiin jää 3 eri lukua
        elif len(self.set) == 3:
            return 3
        # 4 nopista on samoja, settiin jää 2 eri lukua
        elif len(self.set) == 2:
            return 4
        # Kaikki nopista ovat samoja, settiin jää vain 1 luku
        else:
            return 5    

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
