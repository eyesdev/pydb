# pydb

The `pydb` library is a simple Python library that provides basic functionalities for working with a database stored in a text file. It includes functions to add user credentials to the database and to check if given values exist in the database.
Now, I'm going to get into saying how to use this.

#### Installation

First of all, you have to the [Releases](https://github.com/eyesdev/pydb/releases), download the latest version and drag the pydb.py file into your folder that you are editting the file in. Then type `import pydb` in the file ur editting in and congratulations, you have imported pydb!
Now, to use pydb you have to add it to your code.
To have a quick example of pydb, you can open `example.py` which is **in this github repository** or you can look at **this codeblock** to see a quick example of using pydb.

```python
import pydb # Here the library is imported
import time

print('''
...

[1] Make account
[2] Login
[3] Account info (username and password)

''')

option = input(">>> ")

# Here in option 1, you ask the user on the username and password and it adds it to the database.
if option == "1":
    username = input("Enter username: ")
    password = input("Enter password: ")
    pydb.addToDB(username, password) # This line adds it to the database. It takes username and password and puts it into the database.
    time.sleep(3)

if option == "2":
    # Here, this is kind of a checker to see if something exists in a database.
    username = input("Enter username: ")
    password = input("Enter password: ")
    pydb.checkDB(username, password) # Here is uses "checkDB" to check if the user registered an account or not and it tells if it exists.
    time.sleep(3)```


#### Contribution

You can join the [Discord Server](https://discord.gg/N82pwKjwkN) and open a ticket to report bugs and contribute/apply for contribution!
