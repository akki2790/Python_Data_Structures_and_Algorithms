class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[(len(self.items)-1)]

    def size(self):
        return len(self.items)

    
####################

class stack():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class queue():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class dequeue():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.item.insert(0,item)

    def remFront(self):
        return self.items.pop()

    def remRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
