score = int(input("Please enter your age: "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 50 and score < 70:
    print("E")
elif score >= 0 and score < 50:
    print("F")
else:
    print("Wrong Score! Try again!")
