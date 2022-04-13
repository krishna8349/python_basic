def duplicate(arr,n):
    if n==0 or n==1:
        return n
    
    arr.sort();
    j = 1
    
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j += 1

    return j

arr = [1,2,2,3,3,3]
n = len(arr)

n = duplicate(arr, n)

for i in range(n):
    print("%d"%(arr[i]), end=" ")