from collections import deque


def solve():
    # commandsCount = int(input())
    commands = input()
    queueCount = int(input())
    # queueInput = input()[1:-1].split(",")
    queue = deque(input()[1:-1].split(","))

    # 이 값이 True면 정방향, False면 역방향
    sequence_front = True
    error = False

    for i in range(0, len(commands)):
        command = commands[i]

        if command == 'R':
            sequence_front = not sequence_front

        if command == 'D':
            if len(queue) >= 1 and queue[0] != '':
                if sequence_front:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                error = True
                break

        # print(queue)

    if not error:
        print("[", end='')
        queue_len = len(queue)
        if sequence_front:
            for j in range(0, queue_len):
                print(queue.popleft(), end='')
                if j != queue_len - 1:
                    print(",", end='')
        else:
            for j in range(0, queue_len):
                print(queue.pop(), end='')
                if j != queue_len - 1:
                    print(",", end='')
        print("]")
    else:
        print("error")


# solve()
loop = int(input())

for i in range(0, loop):
    solve()
