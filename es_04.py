from . import readline
########################################################################################################################################################
#es_04
def prof_dato_ora_giorno(o, g):
    """
    Trova i professori che insegnano in un'ora e giorno specificati e scrive i loro nomi su un file di testo.

    Args:
        o (str): L'ora in cui cercare i professori.
        g (str): Il giorno in cui cercare i professori.

    Returns:
        None: La funzione non restituisce alcun valore.
    """
    # Apre il file "OrarioTabellaGlobale.csv" in modalità di lettura
    file = open("OrarioTabellaGlobale.csv", "r")
    
    # Apre un nuovo file "es_04.txt" in modalità di scrittura
    file4 = open("es_04.txt", "w")
    
    # Inizializza una lista vuota per memorizzare i nomi dei professori presenti all'ora e giorno specificati
    lista_prof = []
    
    # Itera attraverso le righe del file chiamando la funzione 'readline()'
    for riga in readline.readline():
        # Splitta la riga in una lista di elementi separati dalla virgola
        lista_riga = riga.split(",")
        # Itera attraverso gli elementi della riga
        for elemento in range (len(lista_riga)):
            # controlla se l'elemento corrente corrisponde al giorno specificato
            if lista_riga[elemento].strip()== g:
                # Apro il file OrarioTabellaGlobale.csv in modalità lettura
                file = open("OrarioTabellaGlobale.csv", "r")
                # Leggo la prima riga e la ignoro
                riga_ora = file.readline()
                # Leggo la seconda riga
                riga_ora = file.readline()
                # Chiudo il file
                file.close()
                # Divido la seconda riga in una lista di elementi separati dalla virgola
                lista_ora = riga_ora.split(",")
                # Verifico se l'elemento corrente della lista corrisponde all'orario 'o'
                if lista_ora[elemento].strip() == str(o):
                    # Se corrisponde, assegno la posizione corrente alla variabile 'posizione'
                    posizione = elemento
    # Itera attraverso le righe del file chiamando la funzione 'readline()'                
    for riga in readline.readline():
        # Splitta la riga in una lista di elementi separati dalla virgola
        lista_riga=riga.split(",")
        # Itera attraverso gli elementi della riga
        for i in lista_riga:
            #controlla se nella posizione giusta non sia presente uno spazio vuoto o 'R'
            if lista_riga[posizione].strip()!="" and lista_riga[posizione].strip()!="R":
                #aggiunge alla lista_prof il professore
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
    #rimuovo in primi 2 elementi da lista_prof poichè sono gli elementi delle prime 2 righe (docente, "")    
    lista_prof.remove(lista_prof[0])
    lista_prof.remove(lista_prof[0])
    
    # Costruisce una stringa iniziale per il file di output
    stringa_iniziale = "Elenco dei professori presenti all'ora " + str(o) + " il giorno " + str(g) + ": " + "\n"
    
    # Scrive la stringa iniziale sul file di output
    file4.write(stringa_iniziale)
    
    # Itera attraverso la lista dei professori e li scrive sul file di output
    for i in lista_prof:
        nome_prof = i.strip() + "\n"  # Rimuove eventuali spazi bianchi e aggiunge un nuovo riga
        file4.write(nome_prof)           
    
    # Chiude entrambi i file dopo aver completato le operazioni
    file.close()
    file4.close()
    
    # La funzione non restituisce alcun valore
    return