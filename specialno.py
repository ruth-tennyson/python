m=int(input())
n=int(input())
for i in range (m,n+1):
  if i<99:
    a=(i//10)+(i%10)
    b=(i//10)*(i%10)
    p=a+b
    if(p==i):
      print(i)