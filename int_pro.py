def int_pro(list1):
    pro=1
    list2=[]
    for item in list1:
        pro=pro*item
    return pro

    for item in list1:
        list2.append(int(pro/item))
    return list2
    print list2

int_pro([1,7,3,4])
