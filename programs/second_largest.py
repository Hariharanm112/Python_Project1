def second_highest(n):
    unique=sorted(set(n))
    second=unique[-2]
    return second
num=[1,2,3,2,4,5,5]
print(second_highest(num))


def second_largeest(n):
    first=second=float('-inf')
    for i in n:
        if i > first:
            second=first
            first=i
        elif i>second and i!=first:
            second=i
    if second==float('-inf'):
         return "no second number"
    return second
num=[1,2,3,4,3,4,6,7]
print(second_largeest(num))