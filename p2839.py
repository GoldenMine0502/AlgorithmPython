N = int(input())

five = 0
three = 0

while N > 0:
    if N >= 5:
        N -= 5
        five += 1
    elif N >= 3:
        N -= 3
        three += 1
    elif N >= 1:
        if five > 0:
            five -= 1
            three += 1
            N += 2
        else:
            break

if N == 0:
    print(three + five)
else:
    print(-1)
