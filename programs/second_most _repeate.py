def vaue(n):
    result={}
    for i in n:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    sorting=sorted(set(result.values()),reverse=True)
    second_repeat=sorting[1]
    print(second_repeat)

    item=result.items()
    repeat=[]
    for j in item:
        if j[1]==second_repeat:
            repeat.append(j[0])

    return repeat
print(vaue("aabbbcccc"))