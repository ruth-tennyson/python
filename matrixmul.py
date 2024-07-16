m,n=map(int,input().split())
a=[]
b=[]
c=[]
for i in range (m):
  r1=list(map(int,input().split()))
  a.append(r1)
  c.append([0]*m)
for i in range (m):
  r2=list(map(int,input().split()))
  b.append(r2)
for i in range (m):
  for j in range (n):
    for k in range (n):
      c[i][j]=c[i][j]+a[i][k]*b[k][j]
for i in range (m):
  for j in range (n):
    print(c[i][j],end=" ")
  print()