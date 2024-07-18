class box:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
        self.temp=None
    def insert(self,data):
        if(self.head==None):
            nn=box(data)
            self.head=nn
            self.temp=nn
        else:
            t=self.head
            while(t!=None):
                if(t.data==data):
                    return
                t=t.next
            nn=box(data)
            self.temp.next=nn
            self.temp=nn
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
        print()
            
    def mid(self):
        sp=self.head
        fp=self.head
        while(fp!=None and fp.next!=None):
            sp=sp.next
            fp=fp.next.next
        print(sp.data)
l=ll()
count=0
a=list(map(int,input().split()))
for i in a:
    l.insert(i)
l.display()
l.mid()