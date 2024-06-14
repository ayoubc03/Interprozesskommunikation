import os

fifo_path1 = '/tmp/myfifo1'
fifo_path2 = '/tmp/myfifo2'
fifo_path3 = '/tmp/myfifo3'

# Funktion zum Erstellen der benannten Pipes
def erstelle_pipes():
    for fifo_path in [fifo_path1, fifo_path2, fifo_path3]:
        if not os.path.exists(fifo_path):
            os.mkfifo(fifo_path)
            print(f"Benannte Pipe '{fifo_path}' wurde erstellt.")
        else:
            print(f"Benannte Pipe '{fifo_path}' existiert bereits.")

# Ausführen der Funktion
erstelle_pipes()
