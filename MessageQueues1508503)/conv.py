import random
import time
import posix_ipc
import sys
import signal

def conv():
    # Erstelle die Message Queues
    conv_queue = posix_ipc.MessageQueue("/conv_queue", posix_ipc.O_CREAT)
    stat_queue = posix_ipc.MessageQueue("/stat_queue", posix_ipc.O_CREAT)

    def signal_handler(sig, frame):
        # Signalhandler für SIGINT (z.B. bei Ctrl+C)
        print('Conv-Prozess beendet.')
        # Schließe die Queues
        conv_queue.close()
        stat_queue.close()
        # Lösche die Queues
        posix_ipc.unlink_message_queue("/conv_queue")
        posix_ipc.unlink_message_queue("/stat_queue")
        # Beende den Prozess
        sys.exit(0)

    # Verbinde SIGINT-Signal mit dem signal_handler
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            # Generiere eine Zufallszahl zwischen 1 und 100
            zufallszahl = random.randint(1, 100)
            # Sende die Zufallszahl an die conv_queue
            conv_queue.send(str(zufallszahl))
            # Sende die Zufallszahl an die stat_queue
            stat_queue.send(str(zufallszahl))
            # Gib die eingefügte Zufallszahl aus
            print(f"Conv: Zufallszahl {zufallszahl} in die Queues eingefügt.")
            # Warte für 2 Sekunden
            time.sleep(2)
        except Exception as e:
            # Gib einen Fehler aus, falls einer auftritt
            print("Ein Fehler ist aufgetreten: ", e)
