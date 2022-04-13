def right_triangle(n):
    #smallest way
    # for i in range(0,n):
        # print(" "*(n-i-1), "*"*(i+1))

    # Normal way
    space = 2*n-2

    for i in range(0,n):
        for j in range(0,space):
            print(end=" ")

        space = space-2
    
        for j in range(0,i+1):
            print("* ",end="")

        print("\r")

right_triangle(5)
