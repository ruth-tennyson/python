class sanjoe:
  def __init__(self,n):
    self.stack=[0]*n
    self.top1=-1
    self.top2=0
  def push1(self,data):
    self.top1+=1
    self.stack[self.top1]=data
  def push2(self,data):
    self.top2-=1
    self.stack[self.top2]=data
  def pop1(self):
    if self.top1==-1:
      print( "Stack underflow. pop from stack 1 failed")
      return -1
    else:
      t=self.stack[self.top1]
      self.top1-=1
      return t
  def pop2(self):
    if self.top2==0:
      print( "Stack underflow. pop from stack 2 failed")
      return -1
    else:
      t=self.stack[self.top2]
      self.top2+=1
      return t
  def trav(self):
    print("Stack 1 Elements:")
    temp=self.top1
    while(temp!=-1):
      print(self.stack[temp],end=" ")
      temp-=1
    temp=self.top2
    print()
    print("Stack 2 Elements:")
    while(temp!=0):
      print(self.stack[temp],end=" ")
      temp+=1
    print()
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
s=sanjoe(m+n)
for i in a:
  s.push1(i)
for i in b:
  s.push2(i)
s.trav()
n=int(input())
m=int(input())
for i in range (n):
  s.pop1()
for i in range (m):
  s.pop2()
s.trav()