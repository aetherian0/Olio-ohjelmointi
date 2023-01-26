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
from minipelit.tuplanoppa import Tuplanoppa
from minipelit.tänäänon import Tänäänon


            
def pelaa(peli) -> None:
    '''
    driveri parametrina saadulle pelille 
    '''
    #  Viisinoppa peli
    if type(peli) == Viisinoppa:
        print(peli.otsikko)
        while True:
            try:
                panos = int(input("Aseta panos väliltä 1-100: "))

                # Vaihtoehdot sille monessako nopassa on sama silmäluku
                if peli.tarkista() == 5:
                    print(f"Kaikkien noppien silmäluvut olivat samat, voitit {str(panos * 5000)} pistettä!")
                    
                elif peli.tarkista() == 4:
                    print(f"Neljän eri nopan silmäluku oli sama, voitit {str(panos * 400)} pistettä!")
                    
                elif peli.tarkista() == 3:
                    print(f"Kolmen eri nopan silmäluku oli sama, voitit {str(panos * 30)} pistettä!")
                    
                elif peli.tarkista() == 2:
                    print(f"Kahden eri nopan silmäluku oli sama, voitit {str(panos * 2)} pistettä!")
                    
                else:
                    print(f"Kaikkien noppien silmäluku oli eri, hävisit {str(panos)} pistettä!")

                # Peli päättyi, aloitatko pelin alusta?
                if input('Haluatko pelata uudelleen [K|E]? ').upper() == 'K':
                        uudestaan(peli)
                        clear()
                else:
                    break

            except Exception as e:
                print('OOPS, tarkista syötteesi!', e)



    # Tuplanoppa peli        
    elif type(peli) == Tuplanoppa:
        print(peli.otsikko)
        while True:
            try:
                arvaus = input("Onko kahden nopan summa yli, alle vai tasan 7? \nAnna vastaus tähän: ")
                if peli.tarkista(arvaus):
                    print(f"{arvaus} on oikein, noppien summa oli {peli.noppa_summa}!")
                    if input('Haluatko pelata uudelleen [K|E]? ').upper() == 'K':
                        uudestaan(peli) 
                        clear()
                    else:
                        break
                else:
                    print(f"Vastauksesi on väärin! Oikea vastaus oli {peli.noppa_summa}")
                    if input('Haluatko pelata uudelleen [K|E]? ').upper() == 'K':
                        uudestaan(peli) 
                        clear()
                    else:
                        break

            except Exception as e:
                print('OOPS, tarkista syötteesi!', e)


    # Muussa tapauksessa aloita ArvaaLuku peli   
    else:    
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
    # Käynnistä tänään on peli ohjelman käynnistyessä
    peli = Tänäänon()
    while True:
        try:
            print(f"{peli.lista}")
            arvaus = input("Mikä viikonpäivä yllä olevista päivistä tänään on: ") 
            if peli.tarkista(arvaus):
                print("Vastauksesi on oikein! Tänään on " + peli.tänään)
                break
            else:
                break

        except Exception as e:
                print('OOPS, tarkista syötteesi!', e)

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
                peli = Tuplanoppa()
            case '2':
                peli = Viisinoppa()               
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

 # Käynnistää ohjelman       
if __name__ == '__main__':
    menu()
