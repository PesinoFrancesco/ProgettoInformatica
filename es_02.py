from . import readline

########################################################################################################################################################
#es_02
    
def orario_professore(p):
    """
    Trova l'orario di un professore specificato e chiama la funzione 'numero_ore' per elaborare l'orario.

    Args:
        d (str): Il nome del professore di cui trovare l'orario.

    Returns:
        None: La funzione non restituisce alcun valore, ma chiama 'numero_ore' per elaborare l'orario.

    """
    # Apre il file "OrarioTabellaGlobale.csv" in modalità di lettura
    file = open("OrarioTabellaGlobale.csv", "r")
    
    # Itera attraverso le righe del file chiamando la funzione 'readline()'
    for i in readline.readline():
        # Splitta la riga in una lista di elementi separati dalla virgola
        riga_professore = i.split(",")
        
        # Se il nome del professore nella riga corrente corrisponde al nome specificato
        if riga_professore[0].strip() == d:
            # Assegna l'orario del professore alla variabile 'orario'
            orario = riga_professore 
    
    # Chiude il file dopo aver completato l'operazione
    file.close()

    # Chiama la funzione 'numero_ore' per elaborare l'orario del professore
    numero_ore(orario)
    
    # La funzione non restituisce alcun valore
    return



def numero_ore(o):
    """
    Calcola il numero di ore di lezione presenti nell'orario di un professore e chiama la funzione 'scrittura' per scrivere il risultato.

    Args:
        o (list): Una lista che rappresenta l'orario di un professore.

    Returns:
        None: La funzione non restituisce alcun valore, ma chiama 'scrittura' per scrivere il numero di ore.

    """
    # Inizializza il conteggio delle ore a zero
    num_ore = 0
    
    # Itera attraverso gli elementi dell'orario
    for i in o:
        # Se l'elemento corrente non è una stringa vuota, "R" o "D", incrementa il conteggio delle ore
        if (i.strip() != "" and i.strip() != "R" and i.strip() != "D"):
            num_ore += 1
    
    # Sottrae 1 dal conteggio delle ore per escludere il primo elemento dell'orario
    num_ore -= 1
    
    # Chiama la funzione 'scrittura' per scrivere il numero di ore e l'orario
    scrittura(num_ore, o)
    
    # La funzione non restituisce alcun valore
    return



def scrittura(n, o):
    """
    Scrive l'orario e il numero di ore di un professore su un file di testo.

    Args:
        n (int): Il numero di ore del professore.
        o (list): Una lista che rappresenta l'orario del professore.

    Returns:
        None: La funzione non restituisce alcun valore.
    """
    # Apre il file "OrarioTabellaGlobale.csv" in modalità di lettura
    file = open("OrarioTabellaGlobale.csv", "r")
    
    # Apre un nuovo file "es_02.txt" in modalità di scrittura
    file2 = open("es_02.txt", "w")
    
    # Scrive le prime due righe del file "OrarioTabellaGlobale.csv" sul nuovo file
    c = 1
    riga_prova = file.readline().strip("\n")
    while (riga_prova != "") and (c <= 2):
        file2.write(riga_prova + "\n")
        riga_prova = file.readline().strip("\n")
        c += 1
    
    # Costruisce una stringa contenente l'orario del professore
    stringa_unica = ""
    for stringa in o:
        stringa_unica = stringa_unica + "," + stringa
    stringa_finita = stringa_unica.strip(",")
    
    # Scrive l'orario del professore sul file
    file2.write(stringa_finita)
    
    # Scrive il numero di ore del professore sul file
    numero_ore = "\n" + "Il numero di ore del professore selezionato è: " + str(n)
    file2.write(numero_ore)
    
    # Chiude entrambi i file dopo aver completato le operazioni
    file.close()
    file2.close()
    
    # La funzione non restituisce alcun valore
    return

########################################################################################################################################################