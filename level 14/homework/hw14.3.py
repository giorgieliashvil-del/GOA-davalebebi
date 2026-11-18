# შექმენით ფუნქცია check_even(), რომელსაც გადაეცემა ერთი რიცხვი. ფუნქციამ შეამოწმოს, არის თუ არა რიცხვი ლუწი. თუ ლუწია, დააბრუნოს ტექსტი „ლუწი რიცხვია“, ხოლო სხვა შემთხვევაში — „კენტი რიცხვია“.


def check_even(number):
    if number % 2 == 0:
        print("numbers is even")
    else:
        print("number is odd")


check_even(13)
check_even(10)
check_even(67)
check_even(98)



