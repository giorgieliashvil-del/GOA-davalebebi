

user_number = int(input("please enter your number: "))

i = 1

for i in range(1, user_number, 1):
    print(i)

if user_number % 3 and 5 == 0:
    print("FizzBuzz")

elif user_number % 3 == 0:
    print("Fizz")

elif user_number % 5 == 0:
    print("Buzz")

else:
    print("user_number")
