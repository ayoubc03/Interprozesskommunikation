import socket 
import time 


def log ():

    # Socket erstellen für die Verbindungsaufnahme
    log_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    log_socket.bind(("localhost", 8888)) # Obiges Socket an den Port 8888 binden um Nachrichten empfangen zu können. Localhost bezieht sie auf die lokale Maschine
    log_socket.listen() # Socket dazu anweisen jetzt auf Nachrichten zu warten
    