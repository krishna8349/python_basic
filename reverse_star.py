def reverse_star(n):

    space = n-1

    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end="")

        for j in range(0,space):
            print(end=" ")

        space = n-1

        print("\r")

reverse_star(5)
