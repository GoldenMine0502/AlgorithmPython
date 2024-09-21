N = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(N):
    value = arr[i]

    verify = True

    if value == 1:
        verify = False

    for j in range(2, value):
        if value % j == 0:
            verify = False

    if verify:
        count += 1

print(count)
