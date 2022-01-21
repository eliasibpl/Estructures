#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

import sys

"""
    Calculadora simple amb funció desde el terminal
 
"""

__author__    = "Elias Ibañez"  
__email__    = "eibanezpl@gmail.com"
__license__    = "GPL V3"

def main():
    """
    >>> 1 + 2
    3
    >>> 50 - 30
    20
    >>> 10 % 5
    0
    >>> 200 / 20
    10.0
    >>> 52 // 6
    8
    >>> 12 * 16
    192
    >>> 5 ** 5
    3125
    """
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] =="+":
        print(a + b)
    elif sys.argv[2] =="-":
        print(a - b)
    elif sys.argv[2] =="*":
        print(a * b)
    elif sys.argv[2] =="/":
        print(a / b)
    elif sys.argv[2] =="//":
        print(a // b)
    elif sys.argv[2] =="%":
        print(a % b)
    elif sys.argv[2] =="**":
        print(a ** b)
    else:
        print("Error, formula millor l'operació")
if __name__ == "__main__":
    main()