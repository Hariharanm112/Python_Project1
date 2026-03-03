def next_word(n):
    result=""
    for i in n:
        if i == "z":
            result=result+"a"
        else:
            result=result+chr(ord(i)+1)
    return result
name="abc"
print(next_word(name))