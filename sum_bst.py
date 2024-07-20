class box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class ll:
    def __init__(self):
        self.root=None
    def ins(self,data):
        nn=box(data)
        self.insert(self.root,nn)
    def insert(self,root,nn):
        if self.root==None:
            self.root=nn
            return
        elif nn.data<root.data:
            if root.left!=None:
                self.insert(root.left,nn)
            else:
                root.left=nn
        else:
            if root.right!=None:
                self.insert(root.right,nn)
            else:
                root.right=nn
    def inittrav(self):
      sum=0
      sum=sum+self.tra(self.root)
      return sum
    def tra(self,root):
        if root==None:
            return 0
        else:
            n1=self.tra(root.left)
            n2=self.tra(root.right)
            return root.data+n1+n2
l=ll()
a=int(input())
sum=0
while a!=-1:
  l.ins(a)
  a=int(input())
sum=l.inittrav()
print("Sum of all nodes are",sum)