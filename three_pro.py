def thre_pro(list1):
    list2=[]
    for num1 in list1:
        for num2 in list1:
            for num3 in list1:
                 if num1!=num2 and num2!=num3 and num1!=num3:
                     list2.append(num1*num2*num3)
    return max(list2)

print thre_pro([1,2,3,4,5,6,7])


def wiggle(numbers):
    for n in range(len(numbers)-3):
        if (numbers[n]-numbers[n+1]>0) and (numbers[n+2]-numbers[n+3]<0):
            return "its a wiggle list"

print wiggle([1,7,4,9,2,5])
