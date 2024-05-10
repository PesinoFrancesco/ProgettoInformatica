import os
import sys
from mieifile import readline
sys.path.insert(0,os.path.abspath("."))

from mieifile import es_01
from mieifile import es_02
from mieifile import es_03
from mieifile import es_04

def menu():
    i=input()
    if i.isnumeric()==True:
        i=int(i)
        while i>4 or i<1:
            print ("premi numeri da 1 a 4 per selezionare le funzioni")
            i=int(input())
    
        if i==1:
            c=input("scrivi la classe ES:2BI: ")
            es_01.prof_data_classe(c)

        elif i==2:
            p=input("scrivi il nome di un professore ES:MARCO ROSSI: ")
            es_02.orario_professore(p)
        
        elif i==3:
            p=input("scrivi il nome di un professore ES:MARCO ROSSI: ")
            es_03.numero_d(p)
        
        elif i==4:
            o=input("scrivi una determinata ora del giorno ES:1: ")
            g=input("scrivi un determinato giorno della settimana ES:Lu: ")
            es_04.prof_dato_ora_giorno(o,g)
        
    else:
     print("SEI USCITO DAL PROGRAMMA")

def main():
    print ("-"*80)
    print ("premi numeri da 1 a 4 per selezionare le funzioni")
    print ("premi qualsiasi altro tasto per uscire ")
    menu()
    
if __name__ == '__main__':
    main()

