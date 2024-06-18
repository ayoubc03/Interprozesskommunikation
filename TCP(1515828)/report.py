import socket
import signal
import sys



def report():
    def signal_handler(sig, frame):
        print("\nBeende Report-Prozess...")
        try:
            if verbindung:
                verbindung.close()
            if report_socket:
                report_socket.close()
            print("Verbindung und Socket [REPORT] erfolgreich geschlossen.")
        except Exception as e:
            print("Fehler beim Schließen der Sockets:", e)
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    report_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Report Socket einrichten
    report_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    report_socket.bind(("localhost", 8890)) # Report wird auf Port 8890 gebunden
    report_socket.listen(1) # Report hört auf Verbindungen
    verbindung, _ = report_socket.accept() # Akzeptiert eingehende Verbindungen

    try:
        while True:
            daten = verbindung.recv(1024).decode() # daten werden von Stat empfangen
            if not daten: # Falls Daten leer sind
                break
            print("Statistische Daten:", daten) # Daten ausgeben
    except Exception as e:
        print("Ein Fehler ist aufgetreten [REPORT]:", e)
    


if __name__ == "__main__":
    report()