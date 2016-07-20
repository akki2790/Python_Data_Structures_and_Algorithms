def anagram(sen1, sen2):
    list1=[]
    for item in sen1:
        list1.append(item)

    for ele in sen2:
        if ele not in list1:
            return False
    else:
        return True


print anagram('dog', 'odg')

print anagram('lets see what happens', 'happen s see let s what')

print anagram('clint eastwood','old west action')

print anagram('go go go','gggooo')

print anagram('hi man','hi     man')

print anagram('aabbcc','aabbc')


def anagram1(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    return sorted(s1)==sorted(s2)

def anagram2(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()

    if len(s1)!=len(s2):
        return False
    
    count={}

    for letter in s1:
        if letter in count:
            count[letter]+=1
        else:
            count[letter]=1

    for letter in s2:
        if letter in count:
            count[letter]-=1
        else:
            count[letter]=1

    for k in count:
        if count[k]!=0:
            return False

    else:
        return True


print anagram2('dog', 'odg')

print anagram2('lets see what happens', 'happen s see let s what')

print anagram2('clint eastwood','old west action')

print anagram2('go go go','gggooo')

print anagram2('hi man','hi     man')

print anagram2('aabbcc','aabbc')
