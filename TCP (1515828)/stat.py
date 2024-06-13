import socket

def stat():
    # Stat Socket erstellen
    stat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    stat_socket.bind(("localhost", 8889)) # Socket an den Port binden
    stat_socket.listen(1) # Socket wartet auf Daten

    verbindung , _ = stat_socket.accept() # Verbindung wird akzeptiert.  _ ist notwendig, da accept() ein Tupel zurückgibt mit zwei Werten
    

    summe = 0 # Variable für die Summe der Messwerte
    anzahl = 0 # Anzahl der Durchläufe (notwendig für den Durchschnitt)

    try:
        while True:
            messung = verbindung.recv(4).decode() # Daten von Conv.py empfangen. Vier Bytes sind genug für ein INT
            if not messung: # Falls die gesendeten Daten leer sind
                break
            messwert = int(messung) # Daten in int konvertieren (zuvor String wegen decode() )
            summe += messwert 
            anzahl += 1
            durchschnitt = summe / anzahl # Durchschnitt ausrechnen
            print("Summe:", summe, "Anzahl:", anzahl, "Durchschnitt:", durchschnitt)
    
    except Exception as e:
        print("Ein Fehler ist aufgetreten:" , e)

    
    finally:
        verbindung.close()
        stat_socket.close()


if __name__ == "__main__":
    stat_prozess()