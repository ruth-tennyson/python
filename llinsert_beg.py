class box:
  def __init__(self,data):
    self.data=data
    self.next=None
class ll:
  def __init__(self):
    self.head=None
    self.temp=None
  def insertbeg(self,data):
    nn=box(data)
    if(self.head==None):
      self.head=nn
    else:
      nn.next=self.head
      self.head=nn
  def display(self):
    temp=self.head
    while(temp!=None):
      print(temp.data)
      temp=temp.next
l=ll()
while(True):
  n=int(input())
  if(n>0):
    l.insertbeg(n)
  else:
    break
l.display()