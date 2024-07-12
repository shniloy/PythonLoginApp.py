gmail = "niloybd@gmail.com"
username = "111"
password = "111"

EnterGmail = input("Enter Gmail:")
EnterUserName = input("Enter Username:")
EnterPass = input("Enter Password:")

if EnterGmail == EnterUserName == EnterPass or EnterGmail == EnterPass or EnterUserName == EnterPass: 
    print("Login Success")
else:
    print("Login Failed, Please enter a valid Detail")
