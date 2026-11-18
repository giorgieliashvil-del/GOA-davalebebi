# შექმენით ფუნქცია calculator(), რომელსაც გადაეცემა ორი რიცხვი და მათემატიკური ოპერატორი (+, -, *, /). ფუნქციამ if-elif-else კონსტრუქციის გამოყენებით უნდა შეასრულოს შესაბამისი მათემატიკური მოქმედება და დაბეჭდოს მიღებული შედეგი.

def calculator(number1, number2, operator):
    if operator == "+":
        print(number1+number2)
    elif operator == "-":
        print(number1+number2)
    elif operator == "*":
        print(number1+number2)
    elif operator == "/":
        print(number1+number2)
    else:
        print("wrong operator")





calculator(10, 43, "+")
calculator(54, 89, "-")
calculator(64, 94, "*")
calculator(67, 76, "/")

