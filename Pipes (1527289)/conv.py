import random

fifo_path1 = '/tmp/myfifo1'

def generiere_messwert(fifo_path):
#Erzeugung der Zufallszahl(Messwert)
 messwert = random.randint(1,1000)


#Messwert in den Pipe schreiben lassen
with open(fifo_path1, 'w') as fifo:
    fifo.write(str(messwert))
    fifo.write('\n') 
    
    
print(f"Messwert {messwert} wurde in den benannten Pipe '{fifo_path1}' geschrieben.")   

#Ausführen der Funktion
generiere_messwert()
