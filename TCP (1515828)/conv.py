import random
import os
import time

def conv ():
    while True:
        log_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        stat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        log_socket.connect(("localhost", 8888))  # Log-Prozess hört auf Port 8888
        stat_socket.connect(("localhost", 8889))  # Stat-Prozess hört auf Port 8889

    while True:
                messung = random.randint(0, 100)
                print("Generierte Messung:", messung)