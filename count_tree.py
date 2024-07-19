class box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class qu:
    def __init__(self):
        self.que=[[0]]*100
        self.front=-1
        self.rear=-1
    def push(self,data):
        if self.front==-1:
           self.front+=1
           self.rear+=1
           self.que[self.rear]=data
        else:
            self.rear+=1
            self.que[self.rear]=data
    def res(self):
        self.co=self.front
    def pop(self):
      if self.co>self.rear or self.front==-1:
        return -1
      else:
        t=self.que[self.co]
        self.co+=1
        return t
class ll:
    def __init__(self):
        self.root=None
        self.q=qu()
    def intrav(self):
      count=0
      count=count+self.inorder(self.root)
      print(count)
    def insert(self,data):
        nn=box(data)
        self.q.res()
        if self.root==None:
            self.root=nn
            self.q.push(nn)
        else:
            while(True):
                t=self.q.pop()
                if t==-1:
                  print("Error")
                  break
                if t.left==None:
                    t.left=nn
                    if data!=-1:
                      self.q.push(nn)
                    break
                elif t.right==None:
                    t.right=nn
                    if data!=-1:
                      self.q.push(nn)
                    break
    def inorder(self,root):
        if root==None:
            return 0
        else:
            a=self.inorder(root.left)
            b=self.inorder(root.right)
            if root.data!=-1:
              return a+b+1
            else:
              return 0
l=ll()
list1=list(map(int,input().split()))
for i in list1:
    l.insert(i)
l.intrav()