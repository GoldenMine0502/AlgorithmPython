N = int(input())

arr = list(map(int, input().split()))

# 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는
max = 0

for i in range(0, N):
    value = arr[i]
    if max < value:
        max = value


sum = 0
for i in range(0, N):
    value = arr[i] / max * 100
    sum += value

print(sum / N)