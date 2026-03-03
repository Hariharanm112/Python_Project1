def largest(*n):
    largest=smallest=float("-inf")
    for i in n:
        if i > largest:
            smallest=largest
            largest=i
        elif i > smallest and i != largest:
            smallest=i
        if smallest == float("-inf"):
            return "no"
        else:
            return "it is"
print(largest(1,2,3,4,5))