def highest(n):
    result=0
    for i in n:
        if i >  result:
            result=i
    return result
num=[1,2,3,4,6,4,5]
print(highest(num))