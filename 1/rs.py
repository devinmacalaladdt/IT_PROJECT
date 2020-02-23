import threading
import time
import random
import sys
import socket

#TSHostname set to host running TS when NS entry found
TSHostname = ""

#map hostnames to ip,type
DNSRS = open("PROJI-DNSRS.txt","r")
DNS_TABLE = {}
for line in DNSRS:
    entry = line.split()
    if entry[2]=="NS":
        #TS hostname set
        TSHostname = entry[0]
    else:
        DNS_TABLE[entry[0].lower()] = (entry[1],entry[2])

#open socket
try:
    rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
rs.bind(server_binding)
rs.listen(1)
while 1:

    connection,client = rs.accept()
    while 1:
        #wait for query
        data = connection.recv(200)
        data = data.lower()
        if data:
            print(data)
            if data in DNS_TABLE:
                #if hostname exists, return hostname+ip,type
                connection.send(data.encode('utf-8') + " ".encode('utf-8') + (DNS_TABLE[data])[0].encode('utf-8') + " ".encode('utf-8') + (DNS_TABLE[data])[1].encode('utf-8'))
            else:
                #if doesnt exist, return host of TS and NS type
                connection.send(TSHostname.encode('utf-8') + " - NS".encode('utf-8'))

        else:
            break

    rs.close()

exit()

