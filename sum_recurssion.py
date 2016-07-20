def sum_rec(n):
    if n==0:
        return 0
    else:
        return n+sum_rec(n-1)

print sum_rec(4)

#############

def dig_sum_rec(n):
    sum=0
    while n:
        sum+=n%10
        n/=10
    return sum


print dig_sum_rec(4321)


#############

def word_split(words,word_list):
    list1=[]
    for word in word_list:
        if word in words:
            list1.append(word)

    return list1

print word_split("themanran",["the","ran","man"])

print word_split("themanran",["clown","ran","man"])

print word_split("ilovedogsjohn",["i","love","am","dogs","a","lover","john"])
