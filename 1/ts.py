import threading
import time
import random
import sys
import socket


DNSTS = open("PROJI-DNSTS.txt","r")
DNS_TABLE = {}
for line in DNSTS:
    entry = line.split()
    DNS_TABLE[entry[0].lower()] = (entry[1],entry[2])


try:
    ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
ts.bind(server_binding)
ts.listen(1)
while 1:

    connection,client = ts.accept()
    while 1:

        data = connection.recv(200)
        data = data.lower()
        if data:
            print(data)
            if data in DNS_TABLE:

                connection.send(data.encode('utf-8') + " ".encode('utf-8') + (DNS_TABLE[data])[0].encode('utf-8') + " ".encode('utf-8') + (DNS_TABLE[data])[1].encode('utf-8'))
            else:
                connection.send(data.encode('utf-8') + " - Error:HOST NOT FOUND".encode('utf-8'))

        else:
            break

    ts.close()

exit()



