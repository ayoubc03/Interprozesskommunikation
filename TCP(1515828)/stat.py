import socket
import signal
import sys


def stat():
    def signal_handler(sig, frame):
        print("\nBeende Stat-Prozess...")
        try:
            if verbindung:
                verbindung.close()
            if stat_socket:
                stat_socket.close()
            print("Verbindung und Socket [STAT] erfolgreich geschlossen.")
        except Exception as e:
            print("Fehler beim Schließen der Sockets:", e)
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)

    # Stat Socket erstellen
    stat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    stat_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Report Socket erstellen
    report_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    report_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    while True:
        

        try:
            stat_socket.bind(("localhost", 8889))  # Socket an den Port binden
            stat_socket.listen(1)  # Socket wartet auf eine Verbindung
            
            verbindung, _ = stat_socket.accept()  # Verbindung wird akzeptiert von Conv.py
            
            
            report_socket.connect(("localhost", 8890))  # Report-Prozess auf Port 8890 verbinden
            
            
            summe = 0  # Variable für die Summe der Messwerte
            anzahl = 0  # Anzahl der Durchläufe (notwendig für den Durchschnitt)
        
    
   
            while True:
                messung = verbindung.recv(4).decode() # Daten von Conv.py empfangen. Vier Bytes sind genug für ein INT
                if not messung: # Falls die gesendeten Daten leer sind
                    break
                messwert = int(messung) # Daten in int konvertieren (zuvor String wegen decode() )
                summe += messwert 
                anzahl += 1
                durchschnitt = summe / anzahl # Durchschnitt ausrechnen
                daten = f"Summe: {summe}, Anzahl: {anzahl}, Durchschnitt: {durchschnitt}"
                report_socket.sendall(str(daten).encode())
        
        
        except Exception as e:
            print("Ein Fehler ist aufgetreten: [STAT]" , e)


    
       

if __name__ == "__main__":
    stat()