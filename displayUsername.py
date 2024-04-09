"""
Write a function that accept username and display it    
"""

def usernameInput():
    username = input("Please enter username: ")
    return username


def displayUsername(username):
    print("Username is:  "+ username )
    
username = usernameInput()
displayUsername(username)


