n=int(input())
sum=0
num=n
while n>0:
  a=n%10
  n=n//10
  prod=1
  for i in range(1,a+1):
    prod=prod*i
  sum=sum+prod
if(sum==num):
  print("Yes")
else:
  print("No")