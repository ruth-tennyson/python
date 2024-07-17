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
  def trav(self):
    t=self.head
    if(t!=None):
      print(t.data)
      t=t.next
  def max(self):
    t=self.head
    maxi=t.data
    while t!=None:
      if t.data>maxi:
      	maxi=t.data
    t=t.next
    return(maxi)
l=ll()
while(True):
  n=int(input())
  if(n>0):
    l.insert(n)
  else:
    break
m=l.max()
print(m)
      
      