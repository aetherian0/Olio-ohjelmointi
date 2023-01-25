# -*- coding: utf-8 -*-
'''
Konsoliohjelma minipelikokoelmanlle (proceduraalista ohjelmointia=
Jokainen minipeli on oma luokkansa.
minipelien tuonti (import) ei saa aiheuttaa sivuvaikutuksia.
Hoitaa kaiken käyttäjän ja pelien välisen vuorovaikutuksen. 
'''

import math
import os 
import minipelit
from minipelit.arvaaluku import ArvaaLuku
from minipelit.viisinoppa import Viisinoppa
from minipelit.tänäänon import TänäänOn


            
def pelaa(peli) -> None:
    '''
    driveri parametrina saadulle pelille 
    '''
    #  mikä peli on esim. tarkistamalla sen tyyppi
    if type(peli) == Viisinoppa:
        print(peli.otsikko)
        if input('Haluatko pelata uudelleen [K|E]? ').upper() == 'K':
            uudestaan(peli)
    else:    
        #  testi peli käyttää ArvaaLuku luokkaa
        while True:
            try:
                arvaus = int(input(peli.otsikko + ': '))
                if peli.tarkista(arvaus):
                    print(f"{peli.magic} on oikein ja vain ", \
                      f"{peli.arvaukset} arvauksella!")
                    if input('Haluatko pelata uudelleen [K|E]? ').upper() == 'K':
                        uudestaan(peli)
                        clear()
                    else:
                        break
                else:
                    print('Liian korkea! ' if arvaus > peli.magic else 'Liian matala!')
            except Exception as e:
                print('OOPS, tarkista syötteesi!', e)
            
    
 
def uudestaan(peli):
    '''
    alustaa pelin uudelleen kutsumalla sen reset-metodia
    '''
    peli.reset()
                      
def menu():
    peli = None
    
    while True:
        clear()
        print('''
        Minipelikokoelma:
              
        1. Tuplanoppa
        2. 5-noppa
        3. Testipeli: Arvaa luku
        4. Lopeta
        ''')
        valinta = ''
        while valinta not in ('1', '2', '3'):
            valinta = input('\tValinta: ')
            break
        match valinta: #3.10 or newer
            case '1':
              #  peli = # lisää oma peli oliosi
                print('Tuplanoppa valittu')
            case '2':
                peli = Viisinoppa() # lisää oma peli oliosi
                print('5-noppa valittu')                 
            case '3':
                peli = ArvaaLuku()
            case _:
                break

        if peli:
            pelaa(peli) #  pelaa kunnes peli on valmis ja käyttäjä ei halua uutta peliä
            peli = None #  pelaaja voi valita uuden pelin tai lopettaa

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Windowsissa cls1
        command = 'cls'
    os.system(command)
        
if __name__ == '__main__':
    menu()
