class Node(object):
    
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        
    def reverse(head):
        current=head
        nextnode=None
        previous=None
        
        while current:
            nextnode=current.nextnode
            current.nextnode=previous
            previous=current
            current=nextnode
        return previous
