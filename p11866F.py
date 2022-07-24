import time

N = int(input())
K = int(input())

list = [_ for _ in range(1, N + 1)]
result = []

count = K - 1
while len(list) > 0:
    value = list.pop(count)
    result.append(value)
    count = count + K - 1
    # print(result)
    while count >= len(list) and len(result) < N:
        count -= len(list)
        # print(count)
        # time.sleep(1)

print('<', end='')
for i in range(0, len(result)):
    print(result[i], end='')

    if i != len(result) - 1:
        print(', ', end='')
print('>')