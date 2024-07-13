n=int(input())
for i in range (2,n+1):
  check=0
  for m in range (2,i):
    if i%m==0:
      check=1
      break
  if check!=1:
    print(i,end=" ")