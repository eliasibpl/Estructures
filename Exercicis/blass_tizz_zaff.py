#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

"""
    blass_tizz_zaff.py
    Aquest programa conta del 1 al 110 però substitueix múltiples de 3 s'han de substituir per Blass,
    els que siguin múltiples de 5 per Tizz i els que siguin múltiples de 7 per Zaff. 
    Els que siguin alhora múltiples de 3 i de 5 han de ser substituits per BlassTizz, els que siguin múltiples de 3 i de 7 per BlassZaff, 
    els que siguin múltiples de 5 i de 7 per TizzZaff i els que siguin múltiples de 3, 5 i 7 per BlasTizzZaff. 
 
"""

__author__    = "Elias Ibañez"  
__email__    = "eibanezpl@gmail.com"
__license__    = "GPL V3"

for n in range(110):
    n = n + 1
    if n % 3 == 0:
        n = "Blass"
    elif n % 5 == 0:
        n = "Tizz"
    elif n % 7 == 0:
        n = "Zaff"
    print(n)
