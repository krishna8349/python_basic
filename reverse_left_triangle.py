def reverse_left_triangle(n):
    for i in range(n):
        print("*"*(n-i), " "*(i-n))

reverse_left_triangle(5)