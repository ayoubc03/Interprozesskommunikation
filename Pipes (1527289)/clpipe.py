import os

fifo_path1 = '/tmp/myfifo1'

#Überprüfen, ob die benannte Pipe bereits existiert
if not os.path.exists(fifo_path1):
    #Erstellen der benannten Pipe
    os.mkfifo(fifo_path1)
    print(f"Benannte Pipe '{fifo_path1}' wurde erstellt.")
else:
    print(f"Benannte Pipe '{fifo_path1}' existiert bereits.")    
    