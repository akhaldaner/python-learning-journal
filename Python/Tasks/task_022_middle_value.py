# Middle value
a = int(input())
b = int(input())
c = int(input())

if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)

# AND
if a > b and a < c or a > c and a < b:
    print(a)
elif b > a and b < c or b > c and b < a:
    print(b)
else:
    print(c)

# Algorithmic
if a > b:
    if a < c:
        print(a)  # b < a < c
    elif b > c:
        print(b)  # c < b < a
    else:
        print(c)  # b < c < a
else:
    if c > b:
        print(b)  # a < b < c
    elif c < a:
        print(a)  # c < a < b
    else:
        print(c)  # a < c < b
