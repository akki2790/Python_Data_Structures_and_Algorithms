def finder(list1,list2):
    for item in list1:
        if item not in list2:
            return item
        
print finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])


#######################
import collections

def finder1(list1,list2):
    d=collections.defaultdict(int)

    for num in list2:
        d[num]+=1

    for num in list1:
        if d[num]==0:
            return num
        else:
            d[num]-=1

print finder1([1,2,3,4,5,6,7],[3,7,2,1,4,6])


###############################

list3=[2,3,4,6,7,8]
list4=["a","d","c","v","e","w","p"]

list3.extend(list4)
print list3
