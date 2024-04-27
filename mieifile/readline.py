def readline ():
    
    """
    Legge un file di testo riga per riga e restituisce le righe come una lista.

    Returns:
        list: Una lista contenente le righe del file di testo.

    """
    
    file= open("OrarioTabellaGlobale.csv","r")	# Apre il file in modalità di lettura
    
    lista=[]	# Inizializza una lista vuota per memorizzare le righe del file
    
    # Legge la prima riga del file
    riga_prova=file.readline().strip()
    
    # Continua a leggere finché non si raggiunge la fine del file
    while riga_prova!="":
        lista.append(riga_prova)
        riga_prova=file.readline().strip()
        
    file.close()	# Chiude il file dopo aver completato la lettura
        
    return lista	# Restituisce la lista contenente le righe del file
