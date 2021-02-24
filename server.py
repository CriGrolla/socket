#!/usr/bin/env python3
import socket #importiamo il pacchetto socket
from threading import Thread #importiamo il pacchetto Thread da 'threading'

SERVER_ADDRESS = '127.0.0.1' #indirizzo server
SERVER_PORT = 22224 #porta server

def ricevi_comandi(sock_servive, addr_client): #la funzione riceve la socket connessa al server e la utilizza per accettare le richieste di connessione e per ognuna crea una socket per i dati (sock_service) da cui ricevere le richieste e inviare le risposte
    print("Avviato il thread per servire le richieste da %s" % str(addr_client))
    print("Aspetto di ricevere i dati dell'operazione ")
        while True: #se la connessione è attiva esegue i comandi
            dati = sock_service.recv(2048) #aspetta la richiesta dal client
            if not dati: #controlla che dai abbia un valore
                print("Fine dati dal client. Reset")
                break #se dati non ha valore chiude la connessione
            
            dati = dati.decode() #se dati ha valore lo decodifica
            print("Ricevuto: '%s'" % dati) 
            if dati=='0': 
                print("Chiudo la connessione con " + str(addr_client))
                break #se dati ha valore '0' chiude la connessione
            
            operazione=dati
            op, n1, n2 = dati.split(";") #.split divide la stringa al carattere indicato#Vari if per selezionare l'operazione che il client ha inserito
            if op == "piu": #controllo operazione +
                dati=str(float(n1)+float(n2))
            elif op == "meno": #controllo operazione -
                dati=str(float(n1)-float(n2))
            elif op == "per": #controllo operazione *
                dati=str(float(n1)*float(n2))
            elif op == "diviso": #controllo operazione /
                if n2=='0':
                    dati='Divisione  per zero impossibile.'
                else
                    dati=str(float(n1)/float(n2))

            dati = "Il risultato è: " + str(dati) #output dell'operazione
            print("invio il risultato dell'operazione %s a %s\n" %(operazione, addr_client))
            dati = dati.encode() #codifica la risposta
            sock_service.send(dati) #invia i dati codificati
    sock_service.close() #fine ascolto del server

def ricevi connessioni(sock_listen):
    while True:
        sock_service, addr_client= sock_listen.accept()
        print("\nConnessione ricevuta da %s" %str(addr_client))
        print("Creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("Il thread non si avvia")
            sock_listen.close()

def avvia_server(indirizzo,porta): #crea un endpoint di ascolto (sock_listen) dal quale accettare connessioni in entrata
    try:    
        sock_listen = socket.socket() #crea la socket
        sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #permette di riavviare subito il codice
        sock_listen.bind((indirizzo, porta)) #associa indirizzo e porta. Nota che l'argomento è una tupla:
        sock_listen.listen(5) #imposta quante connessioni pendenti possono essere accodate
        print("Server in ascolto su %s." % str((indirizzo, porta))) #il server è in ascolto e in grado di ricevere richieste di connessione
    except socket.error as errore:
        print(f"Qualcosa è andato storto...\n{errore}")
    ricevi_comandi(sock_listen)

if __name__=='__main__': #consente al nostro codice di capire se stia venendo eseguito come script a se stante, o se è stato richiamato come modulo da qualche programma per usare una o più delle sue varie funzioni e classi
    avvia_server(SERVER_ADDRESS,SERVER_PORT)