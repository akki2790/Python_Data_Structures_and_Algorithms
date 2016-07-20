def pair_sum(arr,k):
    for item1 in arr:
        for item2 in arr:
            if (item1+item2==k):
                return (item1,item2)

print pair_sum([1,3,2,2],4)
print pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)

################

def pair_sum1(arr, k):
    if len(arr)<2:
        print "you cant have a pair with less than 2 numbers"

    seen=set()
    output=set()

    for num in arr:
        target=k-num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num,target), max(num,target)))

    print len(output)
    print "\n".join(map(str,list(output)))


pair_sum1([1,3,2,2],4)
pair_sum1([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
