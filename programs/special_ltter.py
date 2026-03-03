from sys import orig_argv


def name(n):
    string=""
    constant=""
    special=""
    for i in n:
        if i.isalpha():
            if i.lower() in "aeiou":
                string=string+i
            else:
                constant=constant+i
        else:
            special=special+i
    return string+constant+special
print(name("ae$$CDc**io"))