#!/usr/bin/env python3
import socket #importiamo il pacchetto socket
import sys #importiamo il pacchetto sys
import random #importiamo il pacchetto random
import os #importiamo il pacchetto os
import time #importiamo il pacchetto time
import threading #importiamo il pacchetto threading
import multiprocessing #importiamo il pacchetto multiprocessing

SERVER_ADDRESS = '127.0.0.1' #indirizzo server
SERVER_PORT = 22224 #porta server
NUM_WORKERS = 15
def genera_richieste(address, port):
    start_time_thread=time.time()
    print("Client PID: %s, Process Name: %s, Thread Name: &s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name()
        )
    )
    try:
        s=socket.socket() #creazione socke client
        s.connect((address, port)) #connessione al server
        print(f"{threading.current_thread().name} Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n{errore}")
        sys.exit()
    comandi=['piu','meno','per','diviso']
    operazione=comandi[random.randint(0,3)]
    dati=str(operazione)+";"+str(random.randint(1,100))+";"+str(random.randint(1,100))
    dati=dati.encode()
    s.send(dati)
    dati=s.recv(2084)
    if not dati:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    
    dati=dati.decode()
    print(f"{threading.current_thread().name} Ricevuto dal Server:")
    print(dati + '\n')
    dati = "ko"
    dati = dati.encode()
    s.send(dati)
    s.close
    end_time_thread= time.time()
    print(f"{threading.current_thread().name} execution time =", end_time_thread - start_time_thread)

    if __name__ == '__main__':
        #Run tasks using serial function
        start_time= time.time()
        for _ in range(0, NUM_WORKERS):
            genera_richieste(SERVER_ADDRESS, SERVER_PORT)
        end_time= time.time()
        print("Total SERIAL time=", end_time-start_time)
        
        #run tasks using threads
        start_time=time.time()
        threads = [threading.Thread(target=genera_richieste, args=(SERVER_ADDRESS,SERVER_PORT,)) for _ in range(NUM_WORKERS)]
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]
        end_time=time.time()
        print("Total THREADS time = ", end_time-start_time)

        #run tasks using processes
        start_time=time.time()
        processes = [multiprocessing.Process(target=genera_richieste, args=(SERVER_ADDRESS,SERVER_PORT,)) for _ in range(NUM_WORKERS)]
        [process.start() for process in processes]
        [process.join() for process in processes]
        end_time=time.time()
        print("Total PROCESSES time = ", end_time-start_time)