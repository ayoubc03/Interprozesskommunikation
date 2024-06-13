import random
import time
import socket

def conv ():

# Zwei Sockets werden hier erstellt um die Verbindung zu Log und Stat zu gewährleisten
    log_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
    stat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:

        try: # Es wird erst versucht eine Verbindung herzustellen, erst dann wird eine Zahl generiert

            log_socket.connect(("localhost", 8888))  # Log-Prozess listened auf Port 8888
            stat_socket.connect(("localhost", 8889))  # Stat-Prozess listened auf Port 8889

            while True:
                    messung = random.randint(0, 100) # Random Messwert wird generiert 
                    print("Generierte Messung:", messung)

                    log_socket.sendall(str(messung).encode()) # Senden an Log, Daten werden verschl+sselt
                    stat_socket.sendall(str(messung).encode()) # Senden an stat Daten werden verschl+sselt
                    time.sleep(1)  # Eine Sekunde warten zwischen den Verbindungsversuchen

        
        except (ConnectionRefusedError, BrokenPipeError) as e: # Exception falls Verbindung nicht klappt
            print("Verbindung verloren, versuche erneut...", e)
            time.sleep(1)
        
        finally:
            try:
                log_socket.close()  # Log Socket schließen für Ressourcenfreigabe und Stabilität
                stat_socket.close()  # Stat Socket schließen für Ressourcenfreigabe und Stabilität
            except Exception as e:
                print("Fehler beim Schließen der Sockets:", e)


if __name__ == "__main__": # Verhindert, dass das Skript bei einem Import ausgeführt wird
    conv()
    
