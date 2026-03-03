def vowels(n):
    vow="aeiou"
    for i in n:
        if i.lower() in vow:
            print (i)
        else:
            print("it i s not there")
    return True
print(vowels("HAri"))
