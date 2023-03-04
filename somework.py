def sumofn(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
        print(sum)
    return sum

print(sumofn(5))