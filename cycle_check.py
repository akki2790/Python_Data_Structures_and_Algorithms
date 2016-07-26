def cycle_check(node):
    marker1=node
    marker2=node
    while marker!=None and marker2!=None:
        marker1=marker1.nextnode
        marker2=marker2.nextnode.nextnode
        if marker1==marker2:
            return True
    return False
        
