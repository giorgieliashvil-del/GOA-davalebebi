
# მომხმარებელს შეაყვანინეთ ორი რიცხვი: start და end. while ციკლის გამოყენებით გამოიტანეთ ყველა რიცხვი start-დან end-ის ჩათვლით. თუ რიცხვი დადებითია და ლუწია, გამოიტანეთ "Positive Even", სხვა შემთხვევაში გამოიტანეთ თავად რიცხვი.








start = int(input("please enter your first number: "))

end = int(input("please enter your second number: "))

while start < end:
  if start > 0:
    print("positive")
  if start % 2 == 0:
    print("even")
  start += 1


