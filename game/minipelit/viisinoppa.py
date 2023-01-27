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
 

    def aseta_panos(self):
        '''
        Asettaa panoksen suuruuden
        '''
        panos = int(input("Aseta panos väliltä 1-100: "))
        return panos
 

    def tarkista(self):
        '''
        Tarkistaa onko nopissa samoja silmälukuja
        voitto riippuu montako samaa silmälukua nopista löytyy
        '''
        # Kaikki nopat ovat eri, settiin jää 5 eri lukua
        if len(self.set) == 5:
            print(f"Kaikkien noppien silmäluku oli eri, hävisit {str(self.aseta_panos())} pistettä!")

        # 2 nopista on samoja, settiin jää 4 eri lukua
        elif len(self.set) == 4:
            print(f"Kahden eri nopan silmäluku oli sama, voitit {str(self.aseta_panos() * 2)} pistettä!")

        # 3 nopista on samoja, settiin jää 3 eri lukua
        elif len(self.set) == 3:
            print(f"Kolmen eri nopan silmäluku oli sama, voitit {str(self.aseta_panos() * 30)} pistettä!")

        # 4 nopista on samoja, settiin jää 2 eri lukua
        elif len(self.set) == 2:
            print(f"Neljän eri nopan silmäluku oli sama, voitit {str(self.aseta_panos() * 400)} pistettä!")

        # Kaikki nopista ovat samoja, settiin jää vain 1 luku
        else:
            print(f"Kaikkien noppien silmäluvut olivat samat, voitit {str(self.aseta_panos() * 5000)} pistettä!") 


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
