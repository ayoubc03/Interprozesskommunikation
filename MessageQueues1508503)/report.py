import time
import posix_ipc
import sys
import signal

def report_process():
    report_queue = posix_ipc.MessageQueue("/report_queue", posix_ipc.O_CREAT)