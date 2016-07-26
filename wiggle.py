def wiggle(numbers):
    if len(numbers)<2:
        return len(numbers)
    else:
        length=1
        up=None
        for i in xrange(1,len(numbers)):
            if numbers[i-1]<numbers[i] and (up ==None or up==True):
                length+=1
                up=False
            elif numbers[i-1]>numbers[i] and (up ==None or up==False):
                length+=1
                up=True
        return length


print wiggle([1,2,3,4,5,6,7])


def wiggle(numbers):
    if len(numbers)<2:
        return len(numbers)
    length=1
    up=None
    for i in xrange(1,len(numbers)):
        if numbers[i-1]<numbers[i] and (up==None or up==True):
            length+=1
            up=False
        elif numbers[i-1]>numbers[i] and (up==None or up==False):
            length+=1
            up=True

    return length


print wiggle([1,2,3,4,5,6,7])
