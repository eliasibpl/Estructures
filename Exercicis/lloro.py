#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

import sys

"""
    lloro.py
    Aquest programa repeteix el que escriu l'usuari, pararà quan no digui res.
 
"""

__author__    = "Elias Ibañez"  
__email__    = "eibanezpl@gmail.com"
__license__    = "GPL V3"

def main():
    frase_de_usuari = None
    while frase_de_usuari != "":
        frase_de_usuari = input("L'usuari diu: ")
        if frase_de_usuari != "":
            print("El lloro repeteix: " + frase_de_usuari)


if __name__ == "__main__":
    main()