def substring(n):
    max_substring=""
    for i in range(len(n)):
        string=""
        for j in range(i,len(n)):
            if n[j] in string:
                break
            string=string+n[j]
        if len(string) >len(max_substring):
            max_substring=string
    return max_substring
print(substring("abcbcae"))