def prime_number(n):
    if n<=1:
        return False
    for i in range(2,int(n%0.5)+1):
         if n % 2==0:
             return  False
    return True
number=(5,6,7,8,9)
result={num:prime_number(num)for num in number }
print((result))


