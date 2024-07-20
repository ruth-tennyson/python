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
        self.tra(self.root)
    def tra(self,root):
        if root==None:
            return
        else:
            print(root.data,":",sep="",end="")
            if root.left!=None:
                print("L:",root.left.data,",",sep="",end="")
            if root.right!=None:
                print("R:",root.right.data,",",sep="",end="")
            print()
            self.tra(root.left)
            self.tra(root.right)
    def initlim(self,n1,n2):
      self.lim(self.root,n1,n2)
    def lim(self,root,n1,n2):
      if root==None:
        return
      else:
        self.lim(root.left,n1,n2)
        if root.data>=n1 and root.data<=n2:
          print(root.data,end=" ")
        self.lim(root.right,n1,n2)
l=ll()
n=int(input())
list=list(map(int,input().split()))
for i in list:
    l.ins(i)
n1=int(input())
n2=int(input())
l.initlim(n1,n2)