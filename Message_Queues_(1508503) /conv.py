import random
import time
import queue

def conv(conv_queue):
    while True:
        try:
            randzahl = random.randint(0, 100)
            conv_queue.put(randzahl)
            print(f"Zufallszahl {randzahl} in die Queue eingefügt.")
            time.sleep(2)
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)

if __name__ == "__main__":
    conv_queue = queue.Queue()
    conv(conv_queue)