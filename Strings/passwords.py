password = "Pa$$word"
typedPassword = ""
while(typedPassword != password):
    typedPassword = input("Input Password: ")
    if typedPassword == password:
        print("Logged In")
    else:
        print("Wrong Password")
