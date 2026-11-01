
user_number = int(input("Please enter your number: "))

even_sum = 0

for number in range(0, user_number, 2):
    even_sum += number

print(even_sum)