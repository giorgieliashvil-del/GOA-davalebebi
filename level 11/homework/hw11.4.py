
# შექმენით მასივი სახელად ages სადაც შეინახავთ მინიმუმ 10 ადამიანის ასაკს, თქვენი დავალებაა გადაუაროთ მასივს for ციკლით და შეამოწმოთ, იმ შემთხვევაში თუ ადამიანი არის სრულწლოვანი (ანუ ასაკი თუ არის 18 ან მეტი) გამოიტანეთ ტერმინალში "User is Adult!", ყველა სხვა შემთხვევაში გამოიტანეთ ტერმინალში "User is not Adult!".


ages = [15, 16, 17, 18, 19, 20, 21, 22, 23, 34]


for number in ages:
    print(number)


user_age = int(input("please enter your age: "))
if user_age >= 18:
    print("User is adult!")

else:
    print("User is not adult!")

