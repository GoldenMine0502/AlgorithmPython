# asdfasdfasfd
N = int(input())
li = list(map(int, input().split()))
# li = [3, 2, 1, 10]
# li.sort(reverse=True) # N log N = 24
# li = sorted(reverse=True)
# print(li)
max_value = -1000000
min_value = 1000000

for value in li:  # N = 8
    if max_value < value:
        max_value = value

    if min_value > value:
        min_value = value

print(min_value, max_value)


