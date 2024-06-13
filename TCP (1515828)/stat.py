import socket

def stat():
    # Stat Socket erstellen
    stat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    stat_socket.bind(("localhost", 8889)) # Socket an den Port binden
    stat_socket.listen(1) # Socket wartet auf Daten

    verbindung , _ = stat_socket.accept() # Verbindung wird akzeptiert.  _ ist notwendig, da accept() ein Tupel zurückgibt mit zwei Werten