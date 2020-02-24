0. Please write down the full names and netids of both your team members.
    Devin Macalalad dtm97
    Kyle Shteynberg ks1229

1. Briefly discuss how you implemented your recursive client functionality.
    RS and TS both use maps that correspont hostnames read in from their respective files to a tuple containing the
    associated IP and type. For RS, when a entry with type NS is encountered, the hostname of TS is saved. When a client
    connects to either, their request is looked up in the table. If an entry exists, the hostname, IP, and type are
    returned to the client. In the RS, if it doesnt exist, it returns the hostname of TS. In the TS, if it doesnt exist,
    an error is returned. For the client, each line of HNS is sent to RS first and a response is obtained. If the
    response has type A, it is written to the RESOLVED file. Otherwise, a connection is made to TS using the hostname
    returned (only one connection is made after first miss, then the same connection is used for subsequent misses).
    The request is then sent to TS, and the response is written to the file regardless

2. Are there known issues or functions that aren't working currently in your
   attached code? If so, explain.
   There are currently no error checking procedures for inputs (hostnames, ports, invalid file data). So for bad data
   or inputs, unexpected behavior will occur

3. What problems did you face developing code for this project?
   The only problem was trying to open multiple TS connections for each miss in RS. This was remedied by opening one TS
   after the first miss and using it for other misses.

4. What did you learn by working on this project?
   We learned the basics of being able to open, connect, and send data through sockets in python as well as a general
   overview of how DNS requests are processed