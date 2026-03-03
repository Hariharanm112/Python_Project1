def longest_substring(n):
    max_sub=""
    for i in range(len(n)):
        strn=""
        for j in range(i,len(n)):
            if n[j] in strn:
                break
            strn=strn+n[j]
        if len(strn)>len(max_sub):
            max_sub=strn
    return max_sub
print(longest_substring("abacd"))