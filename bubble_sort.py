def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
arr = [4,2,5,3,6,1,0]

bubbleSort(arr)

print("Sorted arr is :")
for i in range(len(arr)):
    print("%d" %arr[i], end=" ")