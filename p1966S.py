from collections import deque
import sys


def solve():
    # 입력 받기
    #  M = 문서의 갯수, I = 인덱스
    M, I = map(int, input().split(" "))

    # 이건 그냥 라인 받아서 split 후 toint
    line = [int(_) for _ in sys.stdin.readline().rstrip().split(" ")]

    # solve
    # 값이랑 인덱스랑 튜플로 묶은 배열
    list = []

    for i in range(0, len(line)):
        list.append((i, line[i]))  # 튜플로 인덱스, 아이템 이렇게 넣는다.

    queue = deque()

    # 일단 다 넣기
    for i in range(0, len(line)):
        queue.append(list[i])

    printed = 0

    while len(queue) > 0:
        local_max = -1

        # 큐를 순회해서 가장 큰 값이 누구인지 확인
        for k in range(0, len(queue)):
            local_max = max(local_max, queue[k][1])

        # 값 하나 빼기
        index, item = queue.popleft()
        if item != local_max:  # !! 최대가 아니면 다시 큐에 넣기 !!
            queue.append((index, item))
        else:  # 이러면 출력이 가능한 상태이므로 큐에 넣지 않음
            printed += 1

            if index == I:  # 근데 당장 출력한 애가 검사가 필요한 인덱스면 현재 출력된 갯수 출력후 종료
                print(printed)
                break


N = int(input())

for i in range(0, N):
    solve()
