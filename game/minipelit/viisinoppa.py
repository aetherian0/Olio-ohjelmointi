import random

class Viisinoppa:
    def __init__(self):
        self.otsikko = "Viisinoppa"
        self.min = 1    # ei vielä käytössä 
        self.max = 100  # ei vielä käytössä 
        self.tulos = 0
        self.alkupotti = 100    # ei vielä käytössä 
        self.potti = 0  # ei vielä käytössä            
        self.__heitot = []
        

    @property
    def heitot(self):
        return self.__heitot

    @heitot.setter
    def heitot(self, value):
        raise ValueError("Nopat ovat vain luettavissa")
 

    def tarkistus(self, panos:int)-> bool:
        '''
        Heittää nopat ja kertoo panoksen mikäli saadaan samoja silmälukuja
        '''
        for i in range(5):
            heitto = random.randint(1,6)
            self.__heitot.append(heitto)
        if len(set(self.__heitot)) == 1: # 5 samaa
            panos *= 5000
            self.tulos = panos
            return True
        elif self.__heitot.count(max(set(self.__heitot), key = self.__heitot.count)) == 4: # 4 samaa
            panos *= 400
            self.tulos = panos
            return True
        elif self.__heitot.count(max(set(self.__heitot), key = self.__heitot.count)) == 3: # 3 samaa
            panos *= 30
            self.tulos = panos
            return True
        elif self.__heitot.count(max(set(self.__heitot), key = self.__heitot.count)) == 2: # 2 samaa
            panos *= 2
            self.tulos = panos
            return True
        else:
            panos *= 0                                                               # 0 samaa
            self.tulos = panos
            return False


    def tallennus(self):
        '''
        Tallennukseen, ei vielä käytössä
        '''
        return 0
    def reset(self):
        '''
        Resetoi olion tilan
        '''
   
        self.otsikko = "Viisinoppa"
        self.min = 1
        self.max = 100
        self.tulos = 0
        self.alkupotti = 100
        self.__heitot = []
