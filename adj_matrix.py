n1 = int(input("Please enter the number of nodes in the graph\n"))
n2 = int(input("Please enter the number of edges in the graph\n"))
c =input("Is the graph directed\n")
l = []
print("Adjacency Matrix Representation:")
for i in range(n1):
  m = [0] * n2
  l.append(m)
for i in range(n1):
  for j in range(n2):
    print(l[i][j],end=" ")
  print()
for i in range(n2):
  s,e,w = (input("Enter the start node, end node and weight of edge no "+str(i+1)+"\n").split())
  if c == "yes":
    l[int(s)-1][int(e)-1] = int(w)
  else:
    l[int(s)-1][int(e)-1] = int(w)
    l[int(e)-1][int(s)-1] = int(w)
print("Adjacency Matrix Representation:")
for i in range(n1):
  for j in range(n2):
    print(l[i][j],end=" ")
  print()