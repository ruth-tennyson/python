mon=int(input())
fib0=0
fib1=1
count=2
while count<mon:
  temp=fib0+fib1
  fib0=fib1
  fib1=temp
  count=count+1
print(fib1)