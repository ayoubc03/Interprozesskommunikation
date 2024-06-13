import os

fifo_path = '/tmp/myfifo'

#Überprüfen, ob die benannte Pipe bereits existiert
if not os.path.exists(fifo_path):
    #Erstellen der benannten Pipe
    os.mkfifo(fifo_path)
    print(f"Benannte Pipe '{fifo_path}' wurde erstellt.")
else:
    print(f"Benannte Pipe '{fifo_path}' existiert bereits.")    
    