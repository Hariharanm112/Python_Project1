def anagaram(s1,s2):
    result1={}

    for i in s1:
        if i in result1:
            result1[i]+=1
        else:
            result1[i]=1
    print(result1)
    result2={}
    for i in s2:
        if i in result2:
            result2[i]+=1
        else:
            result2[i]=1
    print(result2)
    return result1 ==result2
print(anagaram("listen","silent"))


