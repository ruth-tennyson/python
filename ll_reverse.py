class box:
  def __init__(self,data):
    self.data=data
    self.next=None
class ll:
  def __init__(self):
    self.head=None
    self.temp=None
  def insert(self,data):
    nn=box(data)
    if(self.head==None):
      self.head=nn
      self.temp=nn
    else:
      self.temp.next=nn
      self.temp=nn
  def rev(self):
    prev=self.head
    curr=prev.next
    nt=curr.next
    prev.next=None
    while(nt!=None):
        curr.next=prev
        prev=curr
        curr=nt
        nt=nt.next
    curr.next=prev
    self.head.next=None
    self.head=curr
  def display(self):
    temp=self.head
    while(temp!=None):
      print(temp.data,end=' ')
      temp=temp.next
l=ll()
a=input().split()
for i in a:
  n=int(i)
  if(n>0):
    l.insert(n)
  else:
    break
l.rev()
l.display()