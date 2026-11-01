
age = int(input("please enter your age: "))

score = int(input("please enter your score: "))

if age > 18 and score > 70:
    print("You Passed!")

elif age < 18 and score >= 70:
    print("Good result, but you are under 18!")


elif score < 70:
    print("You failed!")
