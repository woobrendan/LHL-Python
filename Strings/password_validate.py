valid = False
while(not valid):
    password = input("Create Password: ")
    repeatPassword = input("Confirm Password: ")
    if len(password) < 8:
        print(
            f"Password was {len(password)} characters long. Passwords must be at least 8 characters long")
    elif password != repeatPassword:
        print("Passwords must be the same")
    else:
        print("Password Saved Successfully")
        valid = True
