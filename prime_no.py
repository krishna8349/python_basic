def check_prime_no(number):
    if number > 1:
        for i in range(2,number):
            if(number % 2)==0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    
    else:
        print(number, "is not a prime number")

check_prime_no(22)


""" TO print a list of prime numbers"""

def prime_number(n):
    for n in range(n):
        if n>1:
            for i in range(2,n):
                if(n%i)==0:
                    break
            else:
                print(n)

prime_number(22)