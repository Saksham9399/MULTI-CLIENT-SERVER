# MULTI-CLIENT-SERVER
A basic computer networking project on multi-client server using sockets in python
#REQUIREMENTS
I have made this project using python and run the test cases on a terminal in mac. In this given file, I have provided the commands used on a terminal in macbook. So if you are using this project on windows command prompt, kindly refer the commands online.

#FILES UPLOADED
The files uploaded along with theis README file are server.py and client.py

#SERVER
To run the file, go to the path location where your file is saved in your UNIX machine. 
Open the terminal and run the command
>> $$ python3 server.py

#CLIENT
To run the file, go to the path location where your file is saved in your UNIX  machine. Make sure to change the local host in the client.py file to host address of your machine. For UNIX machines, the command to find that is >>$$ ifconfig << whereas for windows command prompt, the command used is >> $$ ipconfig <<.

Open the terminal and run the command
>> $$ python3 client.py

To run multiple client windows, you can repeat the above steps using mutiple terminal windows on the same machine, as well as you can open the client.py file at different machines and establish a connection.


<<< Once the connection between the client and server has been established , we run some commands for transfer of data between them>>>


#COMMANDS USED

Once the connection is established, we use "list" command
>> $$ list
This command shows all the active client connections or in our project "Drones" which are connected

After this command, we can use "select"+"space" + "ID no. of the drone" to select the drone to which we want to transfer the delivery details from the server.
>>$$ select 0

After this, the connection is established between the server and a specific client and we can transfer the ADDRESS as well as the ORDER ID to the drone.  

Once the delivery details are  transmitted,the server receives a confirmation message.
