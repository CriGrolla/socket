#!/usr/bin/env python3

input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

import socket #importiamo il pacchetto socket

SERVER_ADDRESS = '127.0.0.1' #indirizzo server
SERVER_PORT = 22224 #porta server

sock_service = socket.socket() #crea la richiesta del servizio

sock_service.connect((SERVER_ADDRESS, SERVER_PORT)) #invia la richiesta del servizio e crea la richiesta

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT))) #comando per verificare che il collegamento sia in funzione
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
    
    dati = dati.encode() #vengono decodificati i dati

    sock_service.send(dati) #vengono inviati i dati

    dati = sock_service.recv(2048) #aspetta la risposta dal server

    if not dati: #controllo risposta del server
        print("Server non risponde. Exit")
        break # se non risponde chiude il collegamento
    
    dati = dati.decode() # se risponde vengono decodificati i dati

    print("Ricevuto dal server:")
    print(dati + '\n') # i dati ricevuti vengono stampati

sock_service.close() #se l'utente inserisce 0 o se il server non risponde, si chiude la connessione