class ViisiNoppaa:  #   muutettu UML luokkakaavion mukaiseksi
    def __init__(self):
        self.otsikko = "ViisiNoppaa" # print("ViisiNoppaa") arvo on None
        self.min = 0
        self.max = 0
        self.noppa1 = 0
        self.noppa2 = 0
        self.noppa3 = 0
        self.noppa4 = 0
        self.noppa5 = 0
 
    def tarkista(self):
        return 0

    def reset(self):
        raise NotImplementedError
