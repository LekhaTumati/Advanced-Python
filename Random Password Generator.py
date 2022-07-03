import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def rand_pass():

    length = int(input("Enter the password length: "))


    random.shuffle(characters)


    password = []
    for i in range(length):
        password.append(random.choice(characters))


    random.shuffle(password)
    print("".join(password))

rand_pass()
