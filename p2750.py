# O(N^2) -> 버블정렬, 셀렉션정렬, 칵테일정렬...
# O(N log N) (위에보단 빠름) -> 퀵정렬(best), 머지정렬, 힙정렬,
# sort() -> 퀵정렬 + 머지정렬 + ...

N = int(input())

arr = []

for i in range(0, N):
    value = int(input())
    arr.append(value)

for i in range(0, N):
    for j in range(0, i):
        if arr[j] > arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for i in range(0, N):
    print(arr[i])
