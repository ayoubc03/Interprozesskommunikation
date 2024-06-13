import socket

def report():
    report_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Report Socket einrichten
    
    report_socket.bind(("localhost", 8890)) # Report wird auf Port 8890 gebunden
    report_socket.listen(1) # Report hört auf Verbindungen
    verbindung, _ = report_socket.accept() # Akzeptiert eingehende Verbindungen

    try:
        while True:
            daten = conn.recv(1024).decode() # daten werden von Stat empfangen
            if not daten: # Falls Daten leer sind
                break
            print("Statistische Daten:", daten) # Daten ausgeben
    except Exception as e:
        print("Ein Fehler ist aufgetreten:", e)
    finally:
        #Sockets schließen, Ressourcen freigeben
        verbindung.close()
        report_socket.close()


if __name__ == "__main__":
    report()