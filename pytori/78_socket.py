import socket

s = socket.socket()
s.connect(("example.com", 80))
s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
print(s.recv(1024).decode())
s.close()