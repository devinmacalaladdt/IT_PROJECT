import sys
import threading
import time
import random
import socket

def client():
    #output file
    f = open("RESOLVED.txt", "w+")
    #open connection to RS
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    port = int(sys.argv[2])
    localhost_addr = socket.gethostbyname(sys.argv[1])
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)
    #ts_opened used to track whether TS opened yet or not
    ts_opened = False
    #iteerate through hostnames from file
    for line in HNS_LIST:
        #send hostname to RS first
        cs.send(line.encode('utf-8'))
        data_from_server = cs.recv(200)

        #NS returned from RS
        if data_from_server.__contains__(" - NS"):
            if ts_opened is False:
                #open TS connection
                localhost_addr2 = data_from_server[0:len(data_from_server) - 5]
                try:
                    cs2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                except socket.error as err:
                    print('socket open error: {} \n'.format(err))
                    exit()
                port2 = int(sys.argv[3])
                cs2.connect((localhost_addr2, port2))
                ts_opened = True
            #send hostname to TS instead
            cs2.send(line.encode('utf-8'))
            data_from_server2 = cs2.recv(200)
            f.write("%s\n" % (data_from_server2))
        else:
            #A returned from RS
            f.write("%s\n" % (data_from_server))

    cs.close()
    cs2.close()
    exit()

#open HNS and add each hostnme to list
HNS = open("PROJI-HNS.txt","r")
HNS_LIST = []
for line in HNS:
    entry = line.split()
    HNS_LIST.append(entry[0])



client()
