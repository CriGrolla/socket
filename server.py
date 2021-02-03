#!/usr/bin/env python3
import socket #importiamo il pacchetto socket

SERVER_ADDRESS = '127.0.0.1' #indirizzo server
SERVER_PORT = 22224 #porta server

sock_listen = socket.socket() #
sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #
sock_listen.bind((SERVER_ADDRESS, SERVER_PORT)) #
sock_listen.listen(5) #

print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT))) #il server è in ascolto e in grado di ricevere richieste di connessione

while True: #se il server è in ascolto esegue i comandi
    sock_service, addr_client = sock_listen.accept() #acetta la connessione con il client e rimane in ascolto per ricevere i dati
    print("\nConnessione ricevuta da " + str(addr_client))
    print("\nAspetto di ricevere i dati ")
    contConn=0 #inizializza il contatore
    while True: #se la connessione è attiva esegue i comandi
        dati = sock_service.recv(2048) #aspetta la richiesta dal client
        contConn+=1 #aumenta il contatore di 1
        if not dati: #controlla che dai abbia un valore
            print("Fine dati dal client. Reset")
            break #se dati non ha valore chiude la connessione
        
        dati = dati.decode() #se dati ha valore lo decodifica
        print("Ricevuto: '%s'" % dati) 
        if dati=='0': 
            print("Chiudo la connessione con " + str(addr_client))
            break #se dati ha valore '0' chiude la connessione
        dati = "Risposta a : " + str(addr_client) + ". Il valore del contatore è : " + str(contConn) #se dati ha valore !='0' restituisce al client il valore del contatore

        dati = dati.encode() #codifica la risposta

        sock_service.send(dati) #invia i dati codificati

    sock_service.close() #fine ascolto del server