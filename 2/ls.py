import threading
import datetime
import random
import sys
import socket
import select


# open socket
try:
    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()


server_binding = ('', int(sys.argv[1]))

#set up info for ts servers
ts1_hostname = socket.gethostbyname(sys.argv[2]);
ts1_port = int(sys.argv[3])
ts2_hostname = socket.gethostbyname(sys.argv[4]);
ts2_port = int(sys.argv[5])

#open ts sockets
try:
    ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()
try:
    ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()
server_binding_ts1 = (ts1_hostname, ts1_port)
ts1.connect(server_binding_ts1)
ts1.setblocking(0)
server_binding_ts2 = (ts2_hostname, ts2_port)
ts2.connect(server_binding_ts2)
ts2.setblocking(0)

#start listening for client
ls.bind(server_binding)
ls.listen(1)
while 1:
    #wait for connection
    connection, client = ls.accept()

    #client found, start waiting for query(ies)
    while 1:

        data_client = connection.recv(200)

        if data_client:

            #hostname query received. Send to both ts servers
            data_ts1=""
            data_ts2=""
            ts1.send(data_client)
            ts2.send(data_client)

            #select will attempt to read from the list of sockets given and return sockets that are ready
            #in a list called 'readable'
            #timeout of 5 seconds given
            readable,writeable,err = select.select([ts1,ts2],[],[],5.0)
            #go through list and attempt recv() accordingly
            for s in readable:
                if s is ts1:
                    data_ts1+=s.recv(200)
                elif s is ts2:
                    data_ts2+=s.recv(200)

            #both servers timed out, list is empty, meaning hostname could not be resolved
            if data_ts1=="" and data_ts2=="":
                connection.send(data_client+" - Error:HOST NOT FOUND".encode('utf-8'))
            #only ts1 could resolve
            elif data_ts2=="":
                connection.send(data_ts1.encode('utf-8'))
            #only ts2 could resolve
            else:
                connection.send(data_ts2.encode('utf-8'))

        else:
            # if no more data/disconnect, stop waiting
            break

    ls.close()

exit()

