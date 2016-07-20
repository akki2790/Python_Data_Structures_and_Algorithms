def str_com(string):
    c=0
    x=""
    list1=[]
    for item in string:
        x=item
        while item==x:
            c=+1
        list1.append(str(x))
        list1.append(str(c))

    return "".join(list1)

print str_com("AAABBBCCC")

###############

def compress(s):
    r=""
    l=len(s)

    if l==0:
        return ""
    elif l==1:
        return s+"1"

    last=s[0]
    c=1
    i=1

    while i <l:
        if s[i]==s[i+1]:
            c+=1
        else:
            r=r+s[i]+str(c)
            c=1
        i+=1

    r=r+s[i]+str(c)
    return r

print compress("AAAABBBBBBCCCC")
