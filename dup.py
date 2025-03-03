num = input()
a = list(map(int, num.split()))
i=0
a.sort()
for j in range(len(a)):
  if(a[i]!=a[j]):
    a[i+1] = a[j]
    i+=1  
print(*a,"list")
print(a[:i+1])
