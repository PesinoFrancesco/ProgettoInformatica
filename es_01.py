#import os
#import sys

#sys.path.insert(0,os.path.abspath("."))
from . import readline

########################################################################################################################################################
#es_01

def prof_data_classe(c):
    """
    Trova e scrive su un file i nomi dei professori associati a una determinata classe.

    Args:
        c (str): La classe di cui trovare i professori.

    Returns:
        None: La funzione non restituisce alcun valore, ma scrive i nomi dei professori su un file.

    """
    # Apre il file "OrarioTabellaGlobale.csv" in modalità di lettura
    file = open("OrarioTabellaGlobale.csv", "r")
    
    # Apre un nuovo file "es_01.txt" in modalità di scrittura
    file1 = open("es_01.txt", "w")
    
    # Inizializza una lista vuota per memorizzare i nomi dei professori associati alla classe specificata
    lista_prof = []

    # Itera attraverso le righe del file chiamando la funzione readline
    for riga in readline.readline():
        # Splitta la riga in una lista di elementi separati dalla virgola
        lista_riga = riga.split(",")
        
        # Itera attraverso gli elementi della riga
        for elemento_riga in lista_riga:
            # Se l'elemento corrente corrisponde alla classe specificata
            if elemento_riga == c:
                # Aggiunge il nome del professore alla lista dei professori associati alla classe
                lista_prof.append(lista_riga[0])
                
                # Inizializza un contatore per contare le occorrenze del professore nella lista
                contatore = 0
                
                # Itera attraverso la lista dei professori
                for professore in lista_prof:
                    # Se il professore corrente è lo stesso della riga corrente
                    if professore == lista_riga[0]:
                        contatore += 1
                        # Se il professore compare più di una volta nella lista, lo rimuove
                        if contatore > 1:
                            lista_prof.remove(professore)
    
    # Costruisce una stringa iniziale per il file di output
    stringa_iniziale = "Elenco dei professori della classe " + str(c) + ": " + "\n"
    
    # Scrive la stringa iniziale sul file di output
    file1.write(stringa_iniziale)
    
    # Itera attraverso la lista dei professori e li scrive sul file di output
    for i in lista_prof:
        nome_prof = i.strip() + "\n"  # Rimuove eventuali spazi bianchi e aggiunge un nuovo riga
        file1.write(nome_prof)
    
    # Chiude entrambi i file dopo aver completato le operazioni
    file.close()
    file1.close


########################################################################################################################################################