import math

# A = [1,6,2,3]
A = [1,1,6]
# def rollDice(A):
count = [0] * 7
for i in A:
    count[i] += 1
min_r = math.inf
for i in range(1,7):
    a = sum(count)
    b = count[i]
    c = count[7-1]
    rotate = a - b + c
    # rotate = sum(count) - count[i] + count[7-i]
    if rotate < min_r:
        min_r = rotate
print(min_r)
# return min_r
# rollDice(A)