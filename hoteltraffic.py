n=int(input())
r=int(input())
d=int(input())
if n in [4,5,6,11,12]:
  c=(r+(r*20)/100)*d
  print(c)
elif n in [1,2,3,7,8,9,10]:
  c=int(r*d)
  print(c)
else:
  print("Invalid Input")