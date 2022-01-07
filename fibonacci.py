from typing import Sequence


number = int(input("How many terms :"))

n1,n2 = 1,2
count = 0

if number<=0:
    print("Please enter a positive integer")
elif number == 1:
    print("fibonacci sequence upto",number,":")
    print(n1)

else:
    print("fibonacci Sequence :")
    while count < number:
        print(n1)
        temp = n1+n2
        n1 = n2
        n2 = temp
        count += 1