
# მომხმარებელს შემოაყვანინეთ მთელი რიცხვი n და for ციკლის დახმარებიუთ შეკრიბეთ ყვცელა ის რიცხვი 1-დან n-ის ჩავლით რომელიც 3-ზე უნაშთოდ იყოფა. საბოლოოდ გამოიტანეთ მიღებული ჯამი



user_number = int(input("Please enter your number: "))

even_sum = 0

for number in range(0, user_number, 3):
    even_sum += number

print(even_sum)


