import random
import string

print("Random password generator")


user_ask = int(input("Enter how many letters of characters you want in your password:"))


chars = string.printable.strip()  


def password_generator():
    password = ""
    for i in range(user_ask):
        new = random.choice(chars)
        password += new
    return password

print("Password using password_generator:")
print(password_generator())


def random_selection():
    random_list = []
    while len(random_list) < user_ask:  
        random_selection = random.choice(chars)
        random_list.append(random_selection)
    return "".join(random_list)


print("Password using random_selection:")
print(random_selection())
