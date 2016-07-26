class squese():
    def __init__(self):
        self.instack=[]
        self.outstack=[]

    def enqueue(self,item):
        self.instack.append(item)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.instack.append(self.outstack.pop())
        
        return self.outstack.pop()
        
    
