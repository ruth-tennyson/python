tc = int(input())
for i in range(tc):
  node, edge = input().split()
  l = [list() for x in range(int(node))]
  for e in range(int(edge)):
    s, e = input().split()
    l[int(s)].append(e)
    l[int(e)].append(s)
  for node, edge in enumerate(l):
      s = str(node)
      if len(edge) > 0:
        s += '-> ' + '-> '.join(edge)
        print(s)