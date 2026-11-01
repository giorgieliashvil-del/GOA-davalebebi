

# შექმენით ცვლადი correct_password = "python123". while ციკლის გამოყენებით მომხმარებელს პაროლი შეაყვანინეთ მანამ, სანამ სწორ პაროლს არ შეიყვანს. არასწორი პაროლის შემთხვევაში გამოიტანეთ "Wrong password!", სწორი პაროლის შემთხვევაში — "Access Granted!".


# i = 1
# while user_password != correct_password:
#     print(i)
#     i += 1

correct_password = "python123"



user_password = ""

while user_password != correct_password:
    user_password = input("please enter your password: ")
    if user_password == correct_password:
        break
    print("Acesses denied")

print("Acesses Granted")











