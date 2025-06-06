l=[7,2,4,1,3]
n=len(l)

for i in range(n):
    current=i
    while current>0 and l[current]<l[current-1]:
        l[current],l[current-1]=l[current-1],l[current]
        current-=1
print(l)
        