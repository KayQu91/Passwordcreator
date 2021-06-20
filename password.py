import secrets
import string


def create_password():

    chars = string.digits + string.ascii_letters + string.punctuation
    password = (''.join(secrets.choice(chars) for i in range(20)))


    passwordlist = open("passwordlist.txt", "a")
    website = input("What´s the website? ")
    email = input("What´s your e-mail? ")
    username = input("What´s your username? ")
    passwordlist.write("Website: " + website + "\n")
    passwordlist.write("E-Mail: " + email + "\n")
    passwordlist.write("Username: " + username + "\n")
    passwordlist.write("Password: " + password + "\n")
    passwordlist.write("-"*30 + "\n")
    passwordlist.close()


create_password()