def non_repeate_word(n):
    result={}
    for i in n:
        if i in result:
            result[i]+=1
        else:
         result[i]=1
    character=""
    for char in n:
        if result[char]==1:
            character=character+char
    return character

print(non_repeate_word("arri"))

