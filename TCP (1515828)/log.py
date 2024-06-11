import socket 
import time 


def log ():

    # Socket erstellen für die Verbindungsaufnahme
    log_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    log_socket.bind(("localhost", 8888)) # Obiges Socket an den Port 8888 binden um Nachrichten empfangen zu können. Localhost bezieht sie auf die lokale Maschine
    log_socket.listen() # Socket dazu anweisen jetzt auf Nachrichten zu warten

    verbindung = log_socket.accept() # Akzeptiert eingehende Daten sofort

try:
    while True:
        messwert = verbindung.recv(4)  # Gesendeter Messwert wird in messwert gespeichert. 4 steht für 4 Bytes-Limit, da ein einziges INT gesendet wird.
        with open("log_datei/log.txt", "a") as f:  # messwert wird in log.txt geschrieben. Wichtig hier "a" für append statt "w" für write
            f.write(messwert + "\n")  # messwert und neue zeile für bessere sichtbarkeit in log.txt


except Exception as e:
    print("Ein Fehler ist aufgetreten: ", e)


finally: 
        verbindung.close() # Verbindung schließen
        log_socket.close() # Socket schließen 


if __name__ == "__main___": # Ausführung des Python-Skripts
    log()