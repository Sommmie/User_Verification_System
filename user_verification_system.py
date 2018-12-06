username = (input('Enter your username: '))
password = [input('Enter your password: ')]
confirmpassword = [input('confirm your password: ')]
pw = password + confirmpassword
signup = {username:pw}
key = list(signup)     #this helps to pick out the key in the dictionary "signup"

#Register
def register():
    if signup[username][0] == signup[username][1]:
        print("Account Created!!!")
    else:
        print("Enter a corresponding password")
        
register()

#login
def login():
    username1 = [input("Enter your username: ")]
    if key == username1:
        password1 = input("Enter your password: ")
        if password1 == signup[username][0]:
            print("Welcome!!!!")
        else:
            print("Ooops!!!, enter a valid password")
    else:
        print("You've entered a wrong username. Please enter the correct username or signup")
login()

