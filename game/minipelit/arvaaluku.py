import random

class ArvaaLuku:
    '''
    ArvaaLuku tietää satunnaisesti generoidut luvut magic väliltä min..max
    ja osaa tarkistaa onko annettu luku magic-listalla ja osaa
    resetoida tilansa
    '''
    def __init__(self, otsikko: str, vali : range, lukuja=1, unique=True)-> None:
        '''
        parametrit:
            otsikko : str, pelin kuvaava nimi
            vali : range esim. range(0, 10)
            lukuja : int, generoitavien lukujen määrä            
            unique: bool, ovatko maagiset luvut unikkeja

        attribuutit:
            otsikko, pelin kuvaava nimi
            vali, väli, josta luvut generoidaan
            unique, unique, ovatko generoidut luvut uniikkeja
            lukuja, generoitavien lukujen määrä
            magic, maagiset luvut (vain luku)
            arvaukset, kaikki arvaukset sekä oikeat että väärät        
        '''

        self.otsikko = otsikko
        self.vali = vali
        self.unique = unique  
        self.lukuja = lukuja
        self.__magic = random.choices(self.vali, k=self.lukuja) #@ver3       
        self.arvaukset = {'oikein':set(), 'väärin':set()} # kaikki arvaukset
        print(self.__magic)

    @property
    def magic(self):
        return self.__magic

    @magic.setter
    def magic(self, value):
        raise ValueError('maaginen luku on vain luettavissa')
       
    @property
    def lukuja(self)->int:
        return self.__lukuja
    
    @lukuja.setter
    def lukuja(self, num:int)->None:
        print(num, len(self.vali))
        if self.unique and 1 <= num < len(self.vali):
            self.__lukuja = num
        elif not self.unique and num >= 1:
            self.__lukuja = num
        else:
            raise ValueError('0 < generoitavien lukujen määrä < väli')

    def tarkista(self, arvaus:int )-> bool:
        '''
        Tarkistaa onko annettu luku magic-listalla ja päivittää arvaukset

        parametrit
            arvaus:int, tarkistettava luku

        return
            bool: True = arvaus on magic-listalla
        '''
        if arvaus in self.magic:
            self.arvaukset['oikein'].add(arvaus)
            return True
        else:
            self.arvaukset['väärin'].add(arvaus)
            return False

    def summa(self, num):
        '''
        palauttaa maagisten lukujen summan ja annetun luvun välisen erotuksen
        '''

        return sum(self.__magic) - num                       
    
    def valmis(self):
        '''
        Tarkistaa onko peli valmis
        return:
            True kaikki numerot on arvattu oikein
        '''
        return self.arvaukset['oikein'] == set(self.__magic)
    
    def reset(self):
        '''
        resetoi olion tilan 
        '''

        self.__magic = random.sample(self.vali, self.lukuja) 
        self.arvaukset  = {'oikein':set(), 'väärin':set()} # kaikki arvaukset
