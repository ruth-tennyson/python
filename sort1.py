n=int(input())
a=[int(input()) for i in range (n)]
temp=0
for i in range (n):
  for j in range (n-i-1):
    if a[j]>a[j+1]:
      temp=a[j]
      a[j]=a[j+1]
      a[j+1]=temp
print("The Sorted array is:")
for i in range (n):
  print(a[i])