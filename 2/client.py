import sys
import threading
import time
import random
import socket


#output file
f = open("RESOLVED.txt", "w+")
#open connection to LS
try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

port = int(sys.argv[2])
localhost_addr = socket.gethostbyname(sys.argv[1])
server_binding = (localhost_addr, port)
cs.connect(server_binding)

#open HNS and iterate through lines
HNS = open("PROJ2-HNS.txt","r")
for line in HNS:
    #send hostname to LS
    cs.send(line.encode('utf-8'))
    data_from_server = cs.recv(200)
    f.write("%s\n" % (data_from_server))
exit()

