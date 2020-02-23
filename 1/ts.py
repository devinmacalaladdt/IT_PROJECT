import threading
import time
import random
import sys
import socket

#map hostname to ip address,type
DNSTS = open("PROJI-DNSTS.txt","r")
DNS_TABLE = {}
for line in DNSTS:
    entry = line.split()
    DNS_TABLE[entry[0].lower()] = (entry[1],entry[2])

#open ts socket
try:
    ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
ts.bind(server_binding)
ts.listen(1)
while 1:
    #wait for connection
    connection,client = ts.accept()
    while 1:

        #recieve query
        data = connection.recv(200)
        data = data.lower()
        if data:
            print(data)
            if data in DNS_TABLE:
                #if hostname exists, return hostname and ip,type
                connection.send(data.encode('utf-8') + " ".encode('utf-8') + (DNS_TABLE[data])[0].encode('utf-8') + " ".encode('utf-8') + (DNS_TABLE[data])[1].encode('utf-8'))
            else:
                #if hostname doesnt exist, return error
                connection.send(data.encode('utf-8') + " - Error:HOST NOT FOUND".encode('utf-8'))

        else:
            break

    ts.close()

exit()



