import random
import time

def conv(conv_queue, stat_queue):
    while True:
        try:
            zufallszahl = random.randint(1, 100)  # Generiere eine Zufallszahl zwischen 1 und 100
            conv_queue.put(zufallszahl)  # Füge die Zufallszahl in die Conv-Queue ein
            stat_queue.put(zufallszahl)  # Füge die Zufallszahl in die Stat-Queue ein
            print(f"Conv: Zufallszahl {zufallszahl} in die Queue eingefügt.")
            time.sleep(2)  # Warte für 2 Sekunden
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)
