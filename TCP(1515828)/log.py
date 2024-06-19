import signal
import socket 
import time 
import sys
import os


def log ():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to log.txt
    log_pfad = os.path.join(script_dir, "log.txt")

    def signal_handler(sig, frame):
        print("\nBeende Log-Prozess...")
        try:
            if verbindung:
                verbindung.close()
            if log_socket:
                log_socket.close()
            print("Verbindung und Socket [LOG] erfolgreich geschlossen.")
        except Exception as e:
            print("Fehler beim Schließen der Sockets:", e)
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    # Socket erstellen für die Verbindungsaufnahme
    log_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    log_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    log_socket.bind(("localhost", 8888)) # Obiges Socket an den Port 8888 binden um Nachrichten empfangen zu können. Localhost bezieht sie auf die lokale Maschine
    log_socket.listen() # Socket dazu anweisen jetzt auf Nachrichten zu warten

    verbindung , _ = log_socket.accept() # Akzeptiert eingehende Daten sofort. _ ist notwendig, da accept() ein Tupel zurückgibt mit zwei Werten


    while True:
        try:
            messwert = verbindung.recv(4) # Gesendeter Messwert wird in messwert gespeichert. 4 steht für 4 Bytes-Limit, da ein einziges INT gesendet wird.
            if not messwert:
                    print("Verbindung geschlossen vom Client")
                    break
            messwert = messwert.decode() 
            with open(log_pfad, "a") as f:  # messwert wird in log.txt geschrieben. Wichtig hier "a" für append statt "w" für write
                f.write(messwert + "\n")  # messwert und neue zeile für bessere sichtbarkeit in log.txt


        except Exception as e:
            print("Ein Fehler ist aufgetreten [LOG]: ", e)


   


if __name__ == "__main__":# Ausführung des Python-Skripts
    log()
