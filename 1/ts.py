import threading
import time
import random
import sys
import socket

DNSTS = open("PROJI-DNSTS.txt","r")
DNS_TABLE = {}
for line in DNSTS:
    entry = line.split()
    DNS_TABLE[entry[0]] = (entry[1],entry[2])

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
ss.bind(server_binding)
ss.listen(1)
csockid = ss.accept()
while 1:

    data = csockid.recv(200)
    if data:
        if data in DNS_TABLE:
            csockid.send(data.encode('utf-8')+" ".encode('utf-8')+(DNS_TABLE[data])[0].encode('utf-8')+" ".encode('utf-8')+(DNS_TABLE[data])[1].encode('utf-8'))
        else:
            csockid.send(data.encode('utf-8')+" - Error:HOST NOT FOUND".encode('utf-8'))

    else:
        break

ss.close()

exit()



