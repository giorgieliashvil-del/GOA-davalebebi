age = int(input("Please enter your age: "))

if age > 0 and age <= 12:
    print("User is child!")
elif age > 12 and age < 18:
    print("User is tinager!")
elif age >= 18 and age < 60:
    print("User is adult!")
elif age >= 60 and age <= 100:
    print("User is old!")
else:
    print("Invalid age!")


