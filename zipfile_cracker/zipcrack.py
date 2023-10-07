# un peu dans le même style que le pdf cracker donc quitte à faire un script autant le faire pour les zip aussi

import zipfile

def crack_password(password_list, obj):
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    obj.extractall(pwd=word)
                    print(f"Password is {word.decode()}")
                    return True
                except:
                    continue
    print("Password not found")
    return False

zip = zipfile.ZipFile("test.zip")
 
crack_password("/usr/share/wordlists/rockyou.txt", zip) 