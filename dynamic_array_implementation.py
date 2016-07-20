import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self,k): #get item at a given index
        if not 0<=k<self.n: #check if the index is in the bounds
            return IndexError("K is out of bounds!")
        else:
            return self.A[k]

    def append(self, ele): # append an element "ele" at the end
        if self.n==self.capacity:
            self._resize(2*self.capacity)#Double capacity if not enough room
        self.A[self.n]=ele #put ele at n(i.e. = length) position of the array A
        self.n+=1

    def _resize(self, new_cap):
        B=self.make_array(new_cap) # make an array B with new_cap
        for item in self.A: 
            B[item]=self.A[item] # put each item in array A into array B

        self.A=B #self array a equal to array B
        self.capacity=new_cap # set the capacity to new capacity

    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)() # return a new array with capacity equal t new capacity

arr = DynamicArray()
arr.append(1)
print len(arr)
print arr[0]
print arr[1]
