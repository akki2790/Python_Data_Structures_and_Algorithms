def balance_check(s):

    if len(s)%2!=0:
        return False

    opening =set("([{")
    matches=[("(",")"),("[","]"),("{","}")]
    stack=[]


    for paran in s:
        if paran in opening:
            stack.append(paran)
        else:
            if len(stack)==0:
                return False
            last_paran=stack.pop()
            if (last_paran,paran) not in matches:
                return False
    return len(stack)==0


print balance_check("{{{(([]))}}}")
