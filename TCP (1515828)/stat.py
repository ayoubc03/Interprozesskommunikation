import socket

def stat():
    # Stat Socket erstellen
    stat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Report Socket erstellen
    report_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
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
            print("Ein Fehler ist aufgetreten:" , e)


    
        finally:
            verbindung.close()
            stat_socket.close()
            report_socket.close()


if __name__ == "__main__":
    stat()