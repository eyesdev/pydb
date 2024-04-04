def addToDB(username, password):
    with open("database.txt", "a") as file:
        file.write(f"{username}:{password}\n")

def checkDB(username, password):
    with open("database.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                print("Success!")
                return
    print("Something went wrong, please try again later.")