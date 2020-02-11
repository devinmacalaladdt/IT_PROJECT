import threading
import time
import random
import sys
import socket

TSHostname = ""
DNSRS = open("PROJI-DNSRS.txt","r")
DNS_TABLE = {}
for line in DNSRS:
    entry = line.split()
    if entry[2]=="NS":
        TSHostname = entry[0]
    else:
        DNS_TABLE[entry[0]] = (entry[1],entry[2])

try:
    rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
rs.bind(server_binding)
rs.listen(1)
csockid = rs.accept()
while 1:

    data = csockid.recv(200)
    if data:
        if data in DNS_TABLE:
            csockid.send(data.encode('utf-8')+" ".encode('utf-8')+(DNS_TABLE[data])[0].encode('utf-8')+" ".encode('utf-8')+(DNS_TABLE[data])[1].encode('utf-8'))
        else:
            csockid.send(TSHostname.encode('utf-8')+" - NS".encode('utf-8'))

    else:
        break

rs.close()

exit()

