import os
import time

fifo_path2 = '/tmp/myfifo2'
fifo_path3 = '/tmp/myfifo3'

def berechne_summe_und_mittelwert():
    # Überprüfen und Erstellen der benannten Pipes, falls sie noch nicht existieren
    if not os.path.exists(fifo_path2):
        os.mkfifo(fifo_path2)
    if not os.path.exists(fifo_path3):
        os.mkfifo(fifo_path3)
    
    summe = 0
    anzahl = 0 
    
    while True:
        # Lesen der Messwerte von der benannten Pipe
        with open(fifo_path2, 'r') as fifo2:
            messwerte = fifo2.readlines()
        
        for messwert in messwerte:
            messwert = messwert.strip()
            if messwert:
                messwert = int(messwert)
                # Berechnung von Summe und Mittelwert der Messwerte
                summe += messwert 
                anzahl += 1
                mittelwert = summe / anzahl 
        
        # Schreiben der Werte in die benannte Pipe
        with open(fifo_path3, 'w') as fifo:
            fifo.write(f"Summe: {summe}\n")
            fifo.write(f"Mittelwert: {mittelwert}\n")
            time.sleep(1)
        # Pause zwischen den Berechnungen
            
        
if __name__ == '__main__':
    berechne_summe_und_mittelwert()
