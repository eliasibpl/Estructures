#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import random

"""
    endeniva.py
    Aquest programa et deixa adivinar un nombre a l'atzar
 
"""

__author__    = "Elias Ibañez"  
__email__    = "eibanezpl@gmail.com"
__license__    = "GPL V3"

def main(numero_secret):
    es_endevinat = False
    suposicio_usuari = None
    while True:
        suposicio_usuari = int(input("Quin número entre 1 i 10 he pensat? "))
        if suposicio_usuari == "":
            print(f"Sento que t'hagis donat per vençut tan ràpid, el número secret era el {numero_secret}")
        elif suposicio_usuari > numero_secret:
            print(f"El número secret és més gran que {suposicio_usuari}, torna a intentar-ho!")
        elif suposicio_usuari < numero_secret:
            print(f"El número secret és més petit que {suposicio_usuari}, torna a intentar-ho!")
        elif suposicio_usuari == numero_secret:
            print(f"Felicitats, l'has encertat era el {numero_secret}!!!")

        

if __name__ == "__main__":
    main(random.randrange(1, 11, 1))