def cake(capacity):
    cake_tuples=[(3,90),(7,160),(2,15)]
    highest_value=0
    hi_va_set=0
    for sets in cake_tuples:
        if (sets[1]/sets[0])>highest_value:
            highest_value=(sets[1]/sets[0])
            hi_va_set=sets
    return highest_value
    return hi_va_set
    print hi_va_set

    count=0
    while capacity!=0:
        


print cake(20)
