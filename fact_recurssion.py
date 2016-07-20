def fac_rec(n):
    if n==0:
        return 1
    return n*fac_rec(n-1)

print fac_rec(5)

