import random

fifo_path = '/tmp/myfifo'

def generate_measurement(fifo_path):
#Erzeugung der Zufallszahl(Messwert)
 messwert = random.randint(1,1000)


#Messwert in den Pipe schreiben lassen
with open(fifo_path, 'w') as fifo:
    fifo.write(str(messwert))
    fifo.write('\n') 
    
    
print(f"Messwert {messwert} wurde in den benannten Pipe '{fifo_path}' geschrieben.")   

#Ausführen der Funktion
generate_measurement()
