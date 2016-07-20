def unique(string):
    list1=list(string)
    for item1 in list1:
        for item2 in list1:
            if item1==item2:
                return False
                print "not unique"
            else:
                return True
                print "unique"

unique("ABCabc")

#########################

def unique2(string):
    list1=[]
    for let in string:
        if let in list1:
            return False
            print "not unique"
        else:
            list1.append(let)
    return True
    print "unique"


unique2("ABCabc")
