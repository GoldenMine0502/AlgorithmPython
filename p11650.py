import sys

N = int(sys.stdin.readline().rstrip())

arr = []

for i in range(0, N):
    a, b = sys.stdin.readline().rstrip().split(" ")
    arr.append([int(a), b])

arr.sort(key=lambda x: (x[0], x[1]))
# for i in range(0, N):
#     for j in range(0, i):
#         if arr[j][0] > arr[i][0] or (arr[j][0] == arr[i][0] and arr[j][1] > arr[i][1]):
#         # if arr[j][1] > arr[i][1]:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

for i in range(0, N):
    print(arr[i][0], arr[i][1])
