import os

fifo_path1 = '/tmp/myfifo1'
dateiname = 'messwerte.txt'

def messwert_in_datei(fifo_path, dateiname):
#Lesen des Messwertes von dem benannten Pipe
 with open(fifo_path, 'r') as fifo:
    messwert = fifo.read()
    
    if not os.path.exists(dateiname):
    #Messwert in eine Datei schreiben
     with open(dateiname, 'w') as datei:
            datei.write(messwert)
            print(f"Die Datei '{dateiname}' wurde erstellt und der Messwert {messwert} wurde in die Datei geschrieben.")
    else:
        print(f"Diese Datei existiert bereits.")
        
        #Überprüfung, ob Messwert in die Datei geschrieben wurde
        if os.path.exists(dateiname):
            with open(dateiname, 'r') as datei:
                gespeicherterMesswert = datei.read()
                print(f"Der gespeicherter Messwert lautet {gespeicherterMesswert}")
        else:
            print('Die Datei/Der Messwert existiert nicht.')
            
            messwert_in_datei(fifo_path1, dateiname)
            
        
        
            
    
    
   