import random

class Tuplanoppa:
    def __init__(self):
        self.otsikko = "Tuplanoppa"
        self.__heitto1 = random.randint(1,6)
        self.__heitto2 = random.randint(1,6)
        self.__sum = self.__heitto1+self.__heitto2
        self.pisteet = 0
        self.panos = int(input("Mikä on panoksesi? (1-100): "))
        self.voitto = self.panos * 100
        self.havio = self.panos * 10


    @property
    def heitto1(self):
        return self.__heitto1

    @property
    def heitto2(self):
        return self.__heitto2

    @property
    def sum(self):
        return self.__sum

    @sum.setter
    def sum(self, value):
        raise ValueError("Summa on vain luettavissa")

	
    def tarkista(self,arvaus):
        '''
        Tarkistaa onko annettu luku sama kuin heitetty summa

        '''
        if (self.__sum == 7) and (arvaus == 7):
            
            return arvaus

        elif self.__sum > 7 and arvaus > 7:
            
            return arvaus 
        
        elif self.__sum < 7 and arvaus < 7:
            
            return arvaus

    def reset(self):
        '''
        resetoi olion tilan 
        '''
        
        self.__heitto1 = random.randint(1,6)
        self.__heitto2 = random.randint(1,6)
        self.__sum = self.__heitto1+self.__heitto2
        self.pisteet = 0
        self.panos = int (input("Mikä on panoksesi? (1-100): "))
        self.arvaus = 0
        self.voitto = self.panos * 100
        self.havio = self.panos * 10
