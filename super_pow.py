# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

def super_pow(a,b,c):
    result=1
    for digit in b:
        result=pow(result,10,c)*pow(a,digit,c)%c
    return result

print super_pow(2,[1,0],1337)
