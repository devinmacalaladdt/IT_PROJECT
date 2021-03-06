import threading
import time
import random
import sys
import socket

# map hostname to ip address,type
DNSTS2 = open("PROJ2-DNSTS2.txt", "r")
DNS_TABLE = {}
for line in DNSTS2:
    #tokenize by spaces
    entry = line.split()
    #map lowercase hostname to IP,Type, and requested hostname (non lowercase)
    DNS_TABLE[entry[0].lower()] = (entry[1], entry[2], entry[0])

# open ts socket
try:
    ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
ts2.bind(server_binding)
ts2.listen(1)
while 1:
    # wait for connection
    connection, client = ts2.accept()

    while 1:

        # ls found, start waiting for query(ies)
        data = connection.recv(200)

        if data:

            if data.lower() in DNS_TABLE:
                # if hostname exists, return hostname and ip,type
                connection.send(
                    (DNS_TABLE[data.lower()])[2].encode('utf-8') + " ".encode('utf-8') + (DNS_TABLE[data.lower()])[0].encode('utf-8') + " ".encode('utf-8') + (DNS_TABLE[data.lower()])[1].encode('utf-8'))
            # hostname doesnt exist, do nothing
        else:
            # if no more data/disconnect, stop waiting
            break

    ts2.close()

exit()



