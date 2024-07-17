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
  def display(self):
    temp=self.head
    while(temp!=None):
      print(temp.data)
      temp=temp.next
l=ll()
while(True):
  n=int(input())
  if(n>0):
    l.insert(n)
  else:
    break
l.display()