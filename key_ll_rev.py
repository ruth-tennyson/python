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
        if self.head==None:
            self.head=nn
            self.temp=nn
        else:
            self.temp.next=nn
            self.temp=nn
    def rev(self,n):
        count=0
        prev=self.head
        curr=self.head.next
        while(count<n-1):
            t1=curr
            t2=curr.next
            curr.next=prev
            prev=t1
            curr=t2
            count+=1
        self.head.next=self.temp
        self.head=t1
        prev=t2
        curr=t2.next
        t2.next=None
        while curr!=None:
            t1=curr
            t2=curr.next
            curr.next=prev
            prev=t1
            curr=t2
        self.temp=prev    
    def trav(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
            
l=ll()
n=list(map(int,input().split()))
for i in n:
    l.insert(i)
n=int(input())
l.rev(n)
l.trav()