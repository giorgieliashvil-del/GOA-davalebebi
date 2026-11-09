
#შექმენით მასივი სახელად mixed_list სადაც შეინახავთ ყველა მონაცემთა ტიპის ელემენტებს (მინიმუმ 10), თქვენი დავალებაა ეს სია შეატრიალოთ (while loop-ი გამოიყენეთ) და ტერმინალში გამოიტანოთ ამ სიის შეტრიალებული ვარიანტი.


mixed_list = ["Gio", 10, 32,3, True, "Saba", 13, 21,2, False, 44, 16,4]


index = len(mixed_list) - 1
result = ""

while index >= 0:
    result += mixed_list[index]

    index -= 1

print(result)



