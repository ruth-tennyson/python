n=int(input())
m=int(input())
print("Enter n")
print("Enter m")
print("The multiplication table of",n,"is")
for i in range (1,m+1):
  print(i,"*",n,"=",(i*n),sep="")