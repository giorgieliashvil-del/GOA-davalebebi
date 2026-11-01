correct_password = "python123"

user_password = input("Please enter your password: ")

while user_password != correct_password:
    print("Wrong, please try again!")
    user_password = input("Please enter your password: ")

print("Access Granted!")