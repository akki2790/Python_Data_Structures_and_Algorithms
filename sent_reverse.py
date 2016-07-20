def sent_reversal(sent):
    list2=[]
    list1=sent.split(" ")
    list2=reversed(list1)
    rev_sent=" ".join(list2)
    print rev_sent

sent_reversal('   Hello John    how are you   ')


###################

def sent_rever2(s):
    return " ".join(reversed(s.split()))

sent_rever2('   Hello John    how are you   ')


#################

def sent_rev3(s):
    words=[]
    space=[" "]

    i=0

    whilei<len(s):
        if s[i] not in space:
            word_start=i

            while i<len(s) and s[i] not in space:
                i+=1
            words.append(s[word_start:i])
        i+=1

    return " ".join(reversed(words))
        
