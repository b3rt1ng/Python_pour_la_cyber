import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(('', 2222)) 
#localhost -> 127.0.0.1
#blank -> listen on all interfaces
soc.listen()

c,a = soc.accept()
c.send(b"Hello, client, send \"quit\" to disconnect\n")
print(f"Connected to {a[0]} at port {a[1]}")
message = c.recv(1024).decode()
while message != "quit\n":
    print(message, end="")
    message = c.recv(1024).decode()
c.send(b"Goodbye, client!\n")
print(f"{a[0]} disconnected")
soc.close()