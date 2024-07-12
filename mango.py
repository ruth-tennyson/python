row=int(input())
col=int(input())
n=int(input())
n=n-1
x=n/row
y=n%col
if x!=(row-1) and y!=0 and y!=(col-1):
  print("No")
else:
  print("Yes")