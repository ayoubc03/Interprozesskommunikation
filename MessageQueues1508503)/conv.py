import random
import time
import posix_ipc
import sys
import signal

def conv():
    conv_queue = posix_ipc.MessageQueue("/conv_queue", posix_ipc.O_CREAT)
    stat_queue = posix_ipc.MessageQueue("/stat_queue", posix_ipc.O_CREAT)

    def signal_handler(sig, frame):
        print('Conv-Prozess beendet.')
        conv_queue.close()
        stat_queue.close()
        posix_ipc.unlink_message_queue("/conv_queue")
        posix_ipc.unlink_message_queue("/stat_queue")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            zufallszahl = random.randint(1, 100)
            conv_queue.send(str(zufallszahl))
            stat_queue.send(str(zufallszahl))
            print(f"Conv: Zufallszahl {zufallszahl} in die Queues eingefügt.")
            time.sleep(2)
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)

if __name__ == "__main__":
    conv()

