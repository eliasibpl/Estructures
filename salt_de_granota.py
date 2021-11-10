#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

import sys

"""
    salt_de_granota.py
    Un programa per fer salts numerics
    
"""

__author__ = "Elias Ibañez"  

def main(inici, final, salt):
    """
    >>>main("")
    """
    for index in range(inici, final, salt):
            print(index, end=" ")
            

            


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
