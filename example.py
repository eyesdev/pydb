from colorama import Fore
import pydb
import time

print(Fore.BLUE + '''
...

[1] Make account
[2] Login
[3] Account info (username and password)

''')

option = input(Fore.BLUE + ">>> ")

if option == "1":
    username = input("Enter username: ")
    password = input("Enter password: ")
    pydb.addToDB(username, password)
    time.sleep(3)

if option == "2":
    username = input("Enter username: ")
    password = input("Enter password: ")
    pydb.checkDB(username, password)
    time.sleep(3)