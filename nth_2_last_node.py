def nth2last(n,head):

    left_pointer=head
    right_pointer=head

    for i in xrange(n-1):
        if not right_pointer.nextnode:
            raise LookupError("Error: n is longer than the linked list")
        right_pointer=right_pointer.nextnode

    while right_pointer.nextnode:
        right_pointer=right_pointer.nextnode
        left_pointer=lfeft_pointer.nextnode

    return left_pointer

class Node:
    def __init__(self,value):
        self.value=value
        self.nextnode=None
