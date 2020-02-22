import sys
import threading
import time
import random
import socket

result = []

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = int(sys.argv[2])
    localhost_addr = socket.gethostbyname(sys.argv[1])
    localhost_addr2 = ""

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    TS_NEEDED = []
    for line in HNS_TABLE:
        cs.send(line.encode('utf-8'))

        # Receive data from the server
        data_from_server = cs.recv(200)

        # if rs comes back empty, connect to ts
        if data_from_server.__contains__(" - NS"):
            localhost_addr2 = data_from_server[0:len(data_from_server) - 5]
            TS_NEEDED.append(line)
        else:
            result.append(data_from_server)



    # send data to server


    # close the client socket
    cs.close()

    if TS_NEEDED:
        try:
            cs2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print('socket open error: {} \n'.format(err))
            exit()
        port2 = int(sys.argv[3])

        # connect to the server on local machine

        cs2.connect((localhost_addr2, port2))

        for line in TS_NEEDED:
            cs2.send(line.encode('utf-8'))

            data_from_server2 = cs2.recv(200)
            result.append(data_from_server2)

        cs2.close()


    f = open("RESOLVED.txt", "w+")
    for line in result:
        f.write("%s\r\n" % (line))

    for line in result:
        print(line)
    exit()

HNS = open("PROJI-HNS.txt","r")
HNS_TABLE = []
for line in HNS:
    entry = line.split()
    HNS_TABLE.append(entry[0])



client()
