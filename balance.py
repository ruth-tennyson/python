class para:
  def __init__(self,n):
    self.struct=[0]*n
    self.top=-1
  def push(self,data):
    self.top+=1
    self.struct[self.top]=data
  def pop(self):
    t=self.struct[self.top]
    self.top-=1
    return t
  def tra(self):
    temp=self.top
    while(temp!=-1):
      print(self.stack[temp])
      temp-=1

n=input()
check=0
p=para(len(n))
for i in range (len(n)):
  if n[i]=='(' or n[i]=='[' or n[i]=='{':
    p.push(n[i])
  elif n[i]==')':
    t=p.pop()
    if t!='(':
      print("Not Balanced")
      check=1
      break
  elif n[i]==']':
    t=p.pop()
    if t!='[':
      print("Not Balanced")
      check=1
      break
  elif n[i]=='}':
    t=p.pop()
    if t!='{':
      print("Not Balanced")
      check=1
      break
if check==0:
  print("Balanced")
    