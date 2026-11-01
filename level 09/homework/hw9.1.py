# მომხმარებელს შემოვაყვანინე ასაკი
user_age = int(input("please enter your age: "))

# თუ მომხმარებელი იქნება 0-ზე ნაკლების წლის მაშინ ტერმინალში გამოვა invalid age
if user_age < 0:
    print("invalid age")
# თუ მომხმარებლი იქნება 18-წელზე ნაკლების ტერმინალში გამოვა adult
elif user_age > 18:
    print("Adult")
# სხვა ყველა შემთხვევაში ტერმინალში გამოვა minor
else:
    print("minor")

