#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

import sys

"""
    #
    #
 
"""

__author__    = "Elias Ibañez"  
__email__    = "eibanezpl@gmail.com"
__license__    = "GPL V3"

def main(inici, final, salt):
    """
    >>> main(10, 20, 2)
    '10, 12, 14, 16, 18, 20'
    >>> main(10, 17, 2)
    '10, 12, 14, 16'
    >>> main(18, 10, -2)
    '18, 16, 14, 12, 10'
    >>> main(18, 20, 0)
    Traceback (most recent call last):
    ...
    ValueError: El valor del salt no pot ser 0
    """
    if salt == 0:
        raise ValueError('El valor del salt no pot ser 0')
    if salt > 0:
        final = final + 1
    else:
        final = final - 1
    resultat = ""
    for index in range(inici, final, salt):
        if index == inici:
            resultat = resultat + str(index) 
        else:
            resultat = resultat + ", " + str(index)
    return resultat
if __name__ == "__main__":
    print(main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))