class BinaryTree(Object):

    def __init__(self,value):
        self.key=value
        self.rightChild=None
        self.leftChild=None

    def insertrightChild(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t

    def insertleftChild(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def setRootVal(self,val):
        self.key=val

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def RootVal(self):
        return self.key
