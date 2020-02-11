import threading
import time
import random
import sys
import socket

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
client.bind(server_binding)
client.listen(1)
csockid = client.accept()