#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

import sys

"""
    qualificacions.py
    Aquest programa es per repetir les qualificacions quan et pregunten del modul.
 
"""

__author__    = "Elias Ibañez"  
__email__    = "eibanezpl@gmail.com"
__license__    = "GPL V3"


def main():
    modul = None
    nota = 0
    nombre_modul = 0

    while modul != "":
        modul = input("Nom del mòdul:")
        if modul != "":
            nota += float(input("Nota del mòdul:"))
            nombre_modul = 1
    if nombre_modul != 0:
        return nota / nombre_modul
    return None

if __name__ == "__main__":
    print(main())