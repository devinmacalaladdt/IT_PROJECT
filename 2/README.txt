0. Please write down the full names and netids of both your team members.
    Devin Macalalad dtm97
    Kyle Shteynberg	ks1229

1. Briefly discuss how you implemented the LS functionality of
   tracking which TS responded to the query and timing out if neither
   TS responded.
    We used non-blocking sockets, specifically select() to track which TS responded as well as give a timeout of 5 sec for no responses. 
    
2. Are there known issues or functions that aren't working currently in your
   attached code? If so, explain.
    There are currently no error checking procedures for inputs (hostnames, ports, invalid file data). So for bad data
    or inputs, unexpected behavior will occur.

3. What problems did you face developing code for this project?
    We didn't have any major issues as this project was very similar to project 1 and used many of the same concepts and code.

4. What did you learn by working on this project?
    We learned how to utilize non-blocking sockets to augment project 1, which we used as a base, and add the new functionality for project 2.
