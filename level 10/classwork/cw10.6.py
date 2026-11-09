
# მომხმარებელს შემოაყვანინეთ დადებითი მთელი რიცხვი. while ციკლის გამოყენებით მიიღეთ ამ ორი რიცხვის შებრუნებული ვერსია მაგალითად: 1234 - 4321


user_number = input("Please enter your number: ")

index = len(user_number) - 1
result = ""

while index >= 0:
    result += user_number[index]

    index -= 1

print(result)



