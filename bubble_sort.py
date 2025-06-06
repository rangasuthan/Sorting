arr=[29,10,14,37,13]
n=len(arr)

for i in range(n):
    swap=False
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            swap=True
            arr[j+1],arr[j]=arr[j],arr[j+1]
    if swap==False:
        break
            
print(arr)