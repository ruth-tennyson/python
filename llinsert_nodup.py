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