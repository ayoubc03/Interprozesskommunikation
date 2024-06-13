
fifo_path = '/tmp/myfifo'
dateiname = 'messwerte.txt'

def messwert_in_datei(fifo_path, dateiname):
#Lesen des Messwertes von dem benannten Pipe
 with open(fifo_path, 'r') as fifo:
    messwert = fifo.read()
    
    if not os.path.exist(dateiname)
    #Messwert in eine Datei schreiben
    with open(dateiname, 'w') as datei:
            datei.write(messwert)
            print(f"Die Datei '{dateiname}' wurde erstellt und der Messwert {messwert} wurde in die Datei geschrieben.")
    else:
        print(f"Diese Datei existiert bereits.")
            
    
    
   