class dequeue():

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def add_front(self,item):
        self.items.append(item)

    def add_rear(self,item):
        self.item.insert(0,item)

    def rem_front(self):
        return self.items.pop()

    def rem_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
