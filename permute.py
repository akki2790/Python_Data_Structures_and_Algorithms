def permute(word):
    result=[]
    if len(word)==1:
        return word
    for i, let in enumerate(word):
        for perm in permute(word[:i]+word[i+1:]):
            result+=[let+perm]
    return result

print permute("abc")
