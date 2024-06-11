import random
import time
import socket

def conv ():

    

    while True:

        try: # Es wird erst versucht eine Verbindung herzustellen, erst dann wird eine Zahl generiert

            # Zwei Sockets werden hier erstellt um die Verbindung zu Log und Stat zu gewährleisten
            log_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            stat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            log_socket.connect(("localhost", 8888))  # Log-Prozess listened auf Port 8888
            stat_socket.connect(("localhost", 8889))  # Stat-Prozess listened auf Port 8889

            while True:
                    messung = random.randint(0, 100) # Random Messwert wird generiert 
                    print("Generierte Messung:", messung)

                    log_socket.sendall(str(messung).encode()) # Senden an Log
                    stat_socket.sendall(str(messung).encode()) # Senden an stat 
                    time.sleep(1)  # Eine Sekunde warten zwischen den Verbindungsversuchen

        
        except (ConnectionRefusedError, BrokenPipeError) as e: # Exception falls Verbindung nicht klappt
            print("Verbindung verloren, versuche erneut...", e)
            time.sleep(1)
        

        finally:
            log_socket.close() # Log Socket schließen für Ressourcenfreigabe und Stabilität
            stat_socket.close() # Stat Socket schließen für Ressourcenfreigabe und Stabilität
