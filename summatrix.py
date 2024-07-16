r =  int(input())
c = int(input())
rw = [0] * r
cw = [0] * c
for i in range(r):
  row = list(map(int, input().split()))
  for j in range(c):
    x = row[j]
    rw[i] += x
    cw[j] += x
 
print("The Sum of rows is", end = " ")
mi = 0
m1 = 1
for i in range(r):
  print(rw[i], end = " ")
  if mi < rw[i]:
    mi = rw[i]
    m1 = i + 1 
print("\nRow", m1, "has a maximum sum")
print("The Sum of columns is", end = " ")
mi = 0
m1 = 1
for i in range(c):
  if mi < cw[i]:
    mi = cw[i]
    m1 = i + 1
  print(cw[i], end = " ") 
print("\nColumn", m1, "has the maximum sum")