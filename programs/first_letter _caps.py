def capital(n):
    split=n.split()
    result=[]
    for i in split:
        result.append(i.capitalize())
    return " ".join(result)
print(capital("hello world"))

print("hello world".title())

