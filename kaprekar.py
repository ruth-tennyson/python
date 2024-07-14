n=int(input())
a=str(n)
num=n**2
l=len(a)
i=10**l
a=num%i
num=num//i
if a+num==n:
  print("Kaprekar Number")
else:
  print("Not a Kaprekar Number")