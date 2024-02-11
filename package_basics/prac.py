import random
import string

char = list(string.ascii_letters + string.digits + "`~!@#$%^&*()_-+=")

def gen_password():
    password_len = int(input('length of password : '))
    random.shuffle(char)
    password = []

    for i in range(password_len):
        password.append(random.choice(char))
    random.shuffle(password)

    print(f'password is {"".join(password)}')

choice = input('enter your choice : ')
if choice == ("y" or "Y"):
    gen_password()
else:
    print('invalid')    