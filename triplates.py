def triplate(arr, n):
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    print(arr[i],arr[j],arr[k])
                    found=True
    
    if found==False:
        print('Not exist')

arr = [0,1,4,-4,-2,3,1]
n = len(arr)
triplate(arr,n)