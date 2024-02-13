import random
import string

char = list(string.ascii_letters + string.digits + "!@#$%^&*()_+-=<>?")


def gen_password():
    password_len = int(input(f'length of password : '))
    random.shuffle(char)
    password = []

    for j in range(password_len):
        password.append(random.choice(char))
    random.shuffle(password)
    print(f'password is {"".join(password)}') # helps to join list indexes


choice = input("do you want to generate a password ? (Y/N) : ")
if choice == 'Y':
    gen_password()
else:
    print('bye')
