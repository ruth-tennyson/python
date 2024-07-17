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
  def dele(self):
    self.head=self.head.next
  def delkey(self,key):
    if self.head.data==key:
      self.head=self.head.next
    else:
        temp=self.head
        while(temp.next.data!=key):
            temp=temp.next
        temp.next=temp.next.next
  def display(self):
    temp=self.head
    while(temp!=None):
      print(temp.data)
      temp=temp.next
l=ll()
n=int(input())
while n>-1:
  l.insert(n)
  n=int(input())
key=int(input())
l.delkey(key)
l.display()
