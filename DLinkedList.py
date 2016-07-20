class DNode:
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        self.prevnode=None

    a=DNode(1)
    b=DNode(2)
    c=DNode(3)

    b.nextnode=c
    a.nextnode=b
    b.prevnode=a
    c.prevnode=b
    
