from . import readline
########################################################################################################################################################
#es_03
def numero_d(p):
    """
    Calcola il numero di ore di disposizione svolte da un professore specificato e scrive il risultato su un file di testo.

    Args:
        d (str): Il nome del professore di cui calcolare il numero di ore di disposizione.

    Returns:
        None: La funzione non restituisce alcun valore.

    """
    # Apre il file "OrarioTabellaGlobale.csv" in modalità di lettura
    file = open("OrarioTabellaGlobale.csv", "r")
    
    # Apre un nuovo file "es_03.txt" in modalità di scrittura
    file3 = open("es_03.txt", "w")

    # Itera attraverso le righe del file chiamando la funzione 'readline()'
    for i in readline.readline():
        # Splitta la riga in una lista di elementi separati dalla virgola
        riga_professore = i.split(",")
        
        # Se il nome del professore nella riga corrente corrisponde al nome specificato
        if riga_professore[0].strip() == d:
            # Assegna l'orario del professore alla variabile 'orario'
            orario = riga_professore 
    
    # Inizializza il conteggio delle ore di disposizione a zero
    num_d = 0
    
    # Itera attraverso gli elementi dell'orario
    for i in orario:
        # Se l'elemento corrente è "D" (disposizione), incrementa il conteggio delle ore di disposizione
        if i.strip() == "D":
            num_d += 1
    
    # Costruisce una stringa contenente il numero di ore di disposizione del professore
    numero_d = "Il numero di ore del professore selezionato è: " + str(num_d)
    
    # Scrive il numero di ore di disposizione sul file
    file3.write(numero_d)
    
    # Chiude entrambi i file dopo aver completato le operazioni
    file.close()
    file3.close()
    
    # La funzione non restituisce alcun valore
    return

########################################################################################################################################################