def reverse(n):
    result=""
    for i in n:
        result=i+result
    return result
print(reverse("name"))