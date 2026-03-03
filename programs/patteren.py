# 1️⃣ Star Pattern
def pattern_stars(n):
    for i in range(n+1):
        print("*"*i)
    print()  # Gap after this pattern

pattern_stars(5)


def pattern_increasing_numbers(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()
    print()  # Gap after this pattern

pattern_increasing_numbers(5)


# 3️⃣ Decreasing Numbers Pattern
def pattern_decreasing_numbers(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end="")
        print()
    print()  # Gap after this pattern

pattern_decreasing_numbers(5)
