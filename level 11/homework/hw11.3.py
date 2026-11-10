
# შექმენით მასივი სახელად mixed_list სადაც შეინახავთ ყველა მონაცემთა ტიპის ელემენტებს (მინიმუმ 10), თქვენი დავალებაა ეს სია შეატრიალოთ (while loop-ი გამოიყენეთ) და ტერმინალში გამოიტანოთ ამ სიის შეტრიალებული ვარიანტი.


mixed_list = ["Saba", "Nika", 10, 20, 20.5, 50.10, True, "Levani", False, 500]

result = []

index = len(mixed_list) - 1

while index >= 0:
    result.append(mixed_list[index])

    index -= 1

print(mixed_list)
print(result)


