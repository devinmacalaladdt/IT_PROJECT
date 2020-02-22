import sys
import threading
import time
import random
import socket

HNS = open("PROJI-HNS.txt","r")
HNS_TABLE = {}
for line in HNS:
    entry = line.split()
    HNS_TABLE = entry[0]

    def client():
        try:
            cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[C]: Client socket created")
        except socket.error as err:
            print('socket open error: {} \n'.format(err))
            exit()

        # Define the port on which you want to connect to the server
        port = int(sys.argv[2])
        localhost_addr = socket.gethostbyname(sys.argv[1])

        # connect to the server on local machine
        server_binding = (localhost_addr, port)
        cs.connect(server_binding)

        # send data to server
        msg = HNS_TABLE[0]
        cs.send(msg.encode('utf-8'))

        # Receive data from the server
        data_from_server = cs.recv(100)
        print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

        # close the client socket
        cs.close()

        # if rs comes back empty, connect to ts
        if data_from_server.__contains__(" - NS"):

            port = int(sys.argv[3])
            localhost_addr = data_from_server[0:len(data_from_server)-5]
            # connect to the server on local machine
            server_binding = (localhost_addr, port)
            cs.connect(server_binding)

            # send data to server
            msg = HNS_TABLE[0]
            cs.send(msg.encode('utf-8'))

            data_from_server = cs.recv(100)
            print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

        exit()

