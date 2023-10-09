# un peu dans le même style que le pdf cracker donc quitte à faire un script autant le faire pour les zip aussi
# note de cour: zip -e file.zip file.txt, -e pour encrypter en mettant un password
#               zip -P password file.zip file.txt, -P pour spécifier le password sauf que forcément la commande reste dans l'historique -> pas secure

#expérimentations update:   j'aimerais tester et voir combien de mdp marchent avec une grosse wordlist (rockyou.txt).
#                           on a quand même environ 0.4% des mdp qui fonctionnent (chokbar)

import zipfile, sys

colors = BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\033[94m', '\033[91m', '\033[0m', '\033[93m', '\033[95m', '\033[92m', '\033[0m'

def crack_password(password_list, obj):
    count = 0
    total = 0
    with open(password_list, 'rb') as file:
        for line in file:
            total += 1
            for word in line.split():
                try:
                    obj.extractall(pwd=word)
                    count += 1
                    # percent = count * 100 / total
                    # sys.stdout.write(f"Password found:{GREEN} {word.decode()}{WHITE} {round(percent, 2)}%\n")
                    # input()
                    # return True
                except:
                    if total % 100000 == 0:
                        percent = count * 100 / total
                        sys.stdout.write(f"{round(percent, 2)}% of words in list are corresponding\n")
                    # print(f"Password {word.decode()} is not correct")
                    continue
    print("Password not found")
    return False

zip = zipfile.ZipFile("test.zip")
 
crack_password("/usr/share/wordlists/rockyou.txt", zip) 