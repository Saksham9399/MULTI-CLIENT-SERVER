import socket
import sys
import threading
import time
from queue import Queue

import pickle


NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9399
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()



def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  

            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0])

        except:
            print("Error accepting connections")


def start_interactive_shell():

    while True:
        cmd = input('SAKSHAM> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized")




def list_connections():
    results = ''
    print("////////////  DRONES AVAILABLE  //////////////")
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))  
            conn.recv(20480)  
        except:
            del all_connections[i]
            del all_address[i]
            continue

        results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"
        print(results)
   


def get_target(cmd):
    try:
        target = cmd.replace('select ', '')  
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to :" + str(all_address[target][0]))
        print(str(all_address[target][0]) + ">", end="")
        return conn
        

    except:
        print("Selection not valid")
        return None



def send_target_commands(conn):

    try:
        address =input("Enter the Address: ")
        conn.send(str.encode(address))
        addr = str(conn.recv(20480), "utf-8")
        print(addr)
    except:
        print("\n Error sending commands")
    try:
        orderid = input("Enter the Order ID: ")
        conn.send(str.encode(orderid))
        ordr = str(conn.recv(20480), "utf-8")
        print(ordr)

    except:  
        print("\n Error sending commands2")
            
  

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            start_interactive_shell()

        queue.task_done()


def jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


create_workers()
jobs()
file.close()
