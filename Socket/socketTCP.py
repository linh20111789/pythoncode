print ('Hello world!')
import socket
from urllib import parse


HOST = "www.cit.ctu.edu.vn"  
PORT = 80        

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
# s.connect(("www.python.org", 80))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('connecting to %s port ' + str(server_address))
s.connect(server_address)


url = parse.urlparse(HOST)
print(url)

print(s.getsockname())

 
# msg = "GET " + HOST[2] + " HTTP/1.0\r\n\r\n" 
# s.sendall(b"HEAD / HTTP/1.1\r\nHost: www.cit.ctu.edu.vn\r\nAccept: text/html\r\n\r\n")

s.sendall(b"GET / HTTP/1.1\r\nHost: www.cit.ctu.edu.vn\r\nAccept: text/html\r\nConnection: close\r\n\r\n")



# data = s.recv(1000000000)
# print('Server: ', data.decode("utf8"))

while True:

    data = s.recv(1024)

    if not data:
        break

    print(data.decode("utf-8"))
