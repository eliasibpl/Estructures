#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

import sys

"""
    Calculadora simple amb funció desde el terminal
 
"""

__author__    = "Elias Ibañez"  
__email__    = "eibanezpl@gmail.com"
__license__    = "GPL V3"

def main(numero1, operador, numero2):
    """
    >>> main (1, "+", 2)
    3
    >>> main (50, "-", 30)
    20
    >>> main (10, "%", 5)
    0
    >>> main (200, "/", 20)
    10.0
    >>> main (52, "//", 6)
    8
    >>> main (12, "*", 16)
    192
    >>> main (5, "**", 5)
    3125
    """

    if operador =="+":
        return(numero1 + numero2)
    elif operador =="-":
        return(numero1 - numero2)
    elif operador =="*":
        return(numero1 * numero2)
    elif operador =="/":
        return(numero1 / numero2)
    elif operador =="//":
        return(numero1 // numero2)
    elif operador =="%":
        return(numero1 % numero2)
    elif operador =="**":
        return(numero1 ** numero2)     
    else:
        return("Error, formula millor l'operació")
if __name__ == "__main__":
    print(main(int(sys.argv[1]),sys.argv[2],int(sys.argv[3])))