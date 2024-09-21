import sys

input = sys.stdin.readline

N, W = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

sum = [0]

avg = arr[0]

verify = True
for i in range(N - 1):
    v = arr[i + 1]
    sum.append(sum[i] + v)

    if abs(v - arr[i]) > W:
        verify = False

totalAvg = sum[N - 1] / (N - 1)
verify &= abs(totalAvg - avg) < W

print("stable" if verify else "unstable")