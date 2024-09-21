a, b = map(int, input().split())

arr = list(map(int, input().split()))

max = 0

for i in range(0, a):
    for j in range(0, a):
        for k in range(0, a):
            if i != j and j != k and k != i:
                sum = arr[i] + arr[j] + arr[k]

                if max < sum <= b:
                    max = sum

print(max)