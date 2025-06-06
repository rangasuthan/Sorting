arr=[7,2,4,1,3]
n=len(arr)

# for i in range(n):
#     current=i
#     while current>0 and l[current]<l[current-1]:
#         l[current],l[current-1]=l[current-1],l[current]
#         current-=1
# print(l)

for i in range(n):
    m=i
    for j in range(i+1,n):
        if arr[m]>arr[j]:
            m=j
    arr[i], arr[m] = arr[m], arr[i]
    
print(arr)