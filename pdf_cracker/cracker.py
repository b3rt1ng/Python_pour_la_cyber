# erreur lors du chargement de rockyou.txt à la lecture du byte 0xf1
# tfaçon python c'est guez donc on va faire ça en rust

import pikepdf, argparse, time

parser = argparse.ArgumentParser(description="PDF Password Cracker")
parser.add_argument("-f", "--file", dest="pdfile", help="PDF file to crack", default="CV_Antoine_psswd.pdf")
parser.add_argument("-w", "--wordlist", dest="psswdlist", help="Password list", default="passwd.txt")

def cracker(pdfile, psswdlist) -> str:
    for password in [i.strip() for i in open(psswdlist)]:
        try:
            with pikepdf.open(pdfile, password=password) as pdf:
                return password
        except pikepdf._core.PasswordError as e:
            continue
    return "Password not found"

start = time.time()
print(cracker(parser.parse_args().pdfile, parser.parse_args().psswdlist))
end = time.time()
print(f"Time taken: {end-start} seconds")
