import os
import time

fifo_path2 = '/tmp/myfifo2'
fifo_path3 = '/tmp/myfifo3'

def berechne_summe_und_mittelwert(fifo_path2, fifo_path3):
    
    summe = 0
    anzahl = 0 
    
    while True:
        # Lesen der messwerte von der benannten Pipe
        with open(fifo_path2, 'w') as fifo:
            messwert = fifo.read()

        messwert = int(messwert)

        # Berechnung von Summe und Mittelwert der Messwerte
        summe += messwert 
        anzahl += 1
        mittelwert= summe / anzahl 
        
        # Schreiben der Werte in die benannte Pipe
        with open(fifo_path3, 'w') as fifo:
            fifo.write(f"Summe: {summe}\n")
            fifo.write(f"Mittelwert: {mittelwert}\n")

        # Pause zwischen den Berechnungen
        time.sleep(1) 
        
        if __name__ == '__main__':
            while True:
                berechne_summe_und_mittelwert(fifo_path2, fifo_path3)
                


