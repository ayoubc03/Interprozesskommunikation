import random
import time
import socket
import signal
import sys

def conv ():
    def signal_handler(sig, frame):
        print("\nBeende Conv-Prozess... ")
        try:
            if log_socket:
                log_socket.close()
            if stat_socket:
                stat_socket.close()
            print("Verbindung und Sockets [CONV] erfolgreich geschlossen.")
        except Exception as e:
            print("Fehler beim Schließen der Sockets:", e)
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)
# Zwei Sockets werden hier erstellt um die Verbindung zu Log und Stat zu gewährleisten
    log_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    log_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    stat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    stat_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:

        try: # Es wird erst versucht eine Verbindung herzustellen, erst dann wird eine Zahl generiert

            log_socket.connect(("localhost", 8888))  # Log-Prozess listened auf Port 8888
            stat_socket.connect(("localhost", 8889))  # Stat-Prozess listened auf Port 8889

            while True:
                    messung = random.randint(0, 100) # Random Messwert wird generiert 
                    print("Generierte Messung:", messung)

                    log_socket.sendall(str(messung).encode()) # Senden an Log, Daten werden in Bytes umgewandelt
                    stat_socket.sendall(str(messung).encode()) # Senden an stat Daten in Bytes umgewandelt
                    time.sleep(1)  # Eine Sekunde warten zwischen den Verbindungsversuchen

        
        except (ConnectionRefusedError, BrokenPipeError) as e: # Exception falls Verbindung nicht klappt
            print("Verbindung verloren, versuche erneut...", e)
            time.sleep(1)
        
    

if __name__ == "__main__": # Verhindert, dass das Skript bei einem Import ausgeführt wird
    conv()
    
