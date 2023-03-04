from re import I


num = int(input("Enter a number ="))

def factorial(num):
    fact = 1
    while (num>1):
        fact *=num
        num -= 1
    print("factorial is = ",fact)

factorial(num)