class box:
  def __init__(self,data,h):
    self.data=data
    self.next=h
class ll:
  def __init__(self):
    self.head=None
    self.temp=None
  def insert(self,data):
    nn=box(data,None)
    if(self.head==None):
      self.head=nn
      self.head.next=self.head
      self.temp=nn
    else:
      self.temp.next=nn
      self.temp=nn
      self.temp.next=self.head
  def trav(self):
    t=self.head
    while(t.next!=self.head):
      print(t.data,end=" ")
      t=t.next
    print(t.data)
l=ll()
n=int(input())
l.insert(n)
while(True):
  n=int(input())
  if n==1:
    n=int(input())
    l.insert(n)
  else:
    break
l.trav()