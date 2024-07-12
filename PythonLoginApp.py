gmail = "niloybd@gmail.com"
username = "111"
password = "111"

print("Login App - Niloy")

EnterGmail = input("Enter Gmail: ")
EnterUsername = input("Enter Username: ")
EnterPassword = input("Enter Password: ")

if (EnterGmail == gmail and EnterUsername == username and EnterPassword == password) or \
   (EnterUsername == username and EnterPassword == password) or \
   (EnterGmail == gmail and EnterPassword == password):
    print("Login Successful")
else:
    print("Login Failed")
