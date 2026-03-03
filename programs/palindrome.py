def palindrome(n):
    rev=""
    for i in n:
        rev=i + rev
    if rev == n:
        return True
    else:
        return False
print(palindrome("madam"))