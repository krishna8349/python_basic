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

check_prime_no(23)