print ('Hello world!')
import socket

HOST = "www.cit.ctu.edu.vn"  
PORT = 80        

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
# s.connect(("www.python.org", 80))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('connecting to %s port ' + str(server_address))
s.connect(server_address)

try:
    while True:
        msg = input('Client: ')
        s.sendall(bytes(msg, "utf8"))

        if msg == "quit":
            break

        data = s.recv(1024)
        print('Server: ', data.decode("utf8"))
finally:
    s.close()

