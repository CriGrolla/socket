#!/usr/bin/env python3
import socket



SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224

sock_listen = socket.socket()

sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

sock_listen.listen(5)

print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))


while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnessione ricevuta da " + str(addr_client))
    print("\nAspetto di ricevere i dati ")
    contConn=0
    while True:
        dati = sock_service.recv(2048)
        contConn+=1
        if not dati:#se non riceve dati chiude la connessione
            print("Fine dati dal client. Reset")
            break
        
        dati = dati.decode()
        print("Ricevuto: '%s'" % dati)
        if dati=='ko':#se riceve ko chiude la connessione
            print("Chiudo la connessione con " + str(addr_client))
            break
        operazione, primo, secondo = dati.split(";")#.split
        #Vari if per selezionare l'operazione che il client ha inserito
        if operazione == "piu":
            risultato = int(primo) + int(secondo)
        if operazione == "meno":
            risultato = int(primo) - int(secondo)
        if operazione == "per":
            risultato = int(primo) * int(secondo)
        if operazione == "diviso":
            risultato = int(primo) / int(secondo)

        dati = "Il risultato dell'operazione: "+operazione +" tra "+primo+" e "+secondo+" è: "+str(risultato)#output

        dati = dati.encode()

        sock_service.send(dati)

    sock_service.close()