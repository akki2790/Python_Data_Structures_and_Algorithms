#Given a positive integer num, write a function which returns True if num is a perfect square else False.

#Note: Do not use any built-in library function such as sqrt.

def perf_sq(number):
    for numbers in range(number/2):
        if numbers**2 == number:
            return True       
    return False


print perf_sq(49)
