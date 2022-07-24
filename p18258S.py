import sys
from collections import deque

queue = deque()
count = int(input())

# print(count)

for i in range(count):
    command = sys.stdin.readline().rstrip().split(" ")

    # print(command)

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
