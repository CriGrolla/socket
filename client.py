#!/usr/bin/env python3
import socket #importiamo il pacchetto socket
import sys #importiamo il pacchetto sys

SERVER_ADDRESS = '127.0.0.1' #indirizzo server
SERVER_PORT = 22224 #porta server

def invia_comandi(socket_service): #la funzione riceve la socket connessa al server e la utilizza per richiedere il servizio
    while True:
        try:
            dati = input("Inserisci i dati da inviare (0 per terminare la connessione): ") #l'utente inserisce la richiesta da mandare al server
        except EOFError: #se trova un errore sulla rete chiude la connessione
            print("\nOkay. Exit")
            break
        if not dati: #controllo che la riga non sia vuota
            print("Non puoi inviare una stringa vuota!") 
            continue
        if dati == '0': 
            print("Chiudo la connessione con il server!") #quando l'utente unserisce '0' in input si interrompe la connessione
            break
        dati = dati.encode() #vengono codificati i dati
        sock_service.send(dati) #vengono inviati i dati
        dati = sock_service.recv(2048) #aspetta la risposta dal server
        if not dati: #controllo risposta del server
            print("Server non risponde. Exit")
            break # se non risponde chiude il collegamento
        dati = dati.decode() # se risponde vengono decodificati i dati
        print("Ricevuto dal server:")
        print(dati + '\n') # i dati ricevuti vengono stampati
    sock_service.close() #se l'utente inserisce 0 o se il server non risponde, si chiude la connessione

def connessione_server(address,port): #crea una socket (s) per una connessione con il server e la passa alla funzione invia_comandi(s)
    try:
        s=socket.socket() #creazione del socket client
        s.connect((address,port)) #connessione al server
        print(f"Connessione al Server: {address}:{port}")
    except s.error as errore: #se si trova un errore si esce
        print(f"Qualcosa è andato storto, sto uscendo... \n{errore}")
        sys.exit()
    invia_comandi(s) #invia i comandi 's'

if __name__=='__main__': #consente al nostro codice di capire se stia venendo eseguito come script a se stante, o se è stato richiamato come modulo da qualche programma per usare una o più delle sue varie funzioni e classi
    avvia_server(SERVER_ADDRESS,SERVER_PORT)