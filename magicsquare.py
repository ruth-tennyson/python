r = int(input())
a = []
for i in range(r):
  a.append([int(x) for x in input().split()])
d1 = 0
d2 = 0
for i in range(r):
  for j in range(r):
    if i == j:
      d1 += a[i][j]
    if i == r - j - 1:
      d2 += a[i][j]
if d1 == d2:
  print("Yes")
else:
  print("No")
