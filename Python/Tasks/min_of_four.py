# Write a program that determines the smallest of four integers.
# The program is given four integers as input.
# The program should print the smallest of the four integers.
# Keep in mind that the smallest integers may be repeated.
# In this case, only one of them should be printed.

# Option 1: pairwise comparison
a = int(input())
b = int(input())
c = int(input())
d = int(input())

first_min = 0
second_min = 0

if a <= b:
    first_min = a
else:
    first_min = b

if c <= d:
    second_min = c
else:
    second_min = d

if first_min <= second_min:
    print(first_min)
else:
    print(second_min)

# Option 2: sequential comparison
a = int(input())
b = int(input())
c = int(input())
d = int(input())

minimum = a

if b < minimum:
    minimum = b
if c < minimum:
    minimum = c
if d < minimum:
    minimum = d

print(minimum)
