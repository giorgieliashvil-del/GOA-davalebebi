# for loop
user_number = int(input("Please enter your number: "))

even_sum = 0

for number in range(0, user_number + 1, 2):
    even_sum += number

print(even_sum)

# while loop
i = 0
while i < user_number:
  i +=(2)

even_sum += i

print(even_sum)
