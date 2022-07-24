import sys
input = sys.stdin.readline
# 입력 받기
dictNames = []
dictPowers = []
powers = []

N, M = map(int, input().split())

for i in range(0, N):
    split = input().split(" ")

    # 쩝.. 클래스 써야 하는데
    dictNames.append(split[0])
    dictPowers.append(int(split[1]))

for i in range(0, M):
    powers.append(int(sys.stdin.readline().rstrip()))


# solve
def binary_search(target, data):
    # data.sort()
    start = 0
    end = len(data) - 1

    while True:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid  # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

        if start > end:
            return mid


for i in range(0, M):
    power = powers[i]

    # 가능한 가장 높은 칭호 구하기
    title = dictNames[0]

    mid = binary_search(power, dictPowers)  # mid - 1, mid, mid + 1 중에서 답이 있음

    if mid > 0 and power > dictPowers[mid - 1]:
        title = dictNames[mid]

    if mid < len(dictPowers) - 1 and power > dictPowers[mid]:
        title = dictNames[mid + 1]

    if mid < len(dictPowers) - 2 and power > dictPowers[mid + 1]:
        title = dictNames[mid + 2]

    # print(title, mid)
    print(title)
