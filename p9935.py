from collections import deque

text = input()
tnt = input()

deque = deque()

frula = False

for ch in text:
    deque.append(ch)

    # 가장 스택의 위에 문자열이 있는지 확인

    # print(deque)

    if len(deque) >= len(tnt):
        index = 0
        while index < len(tnt):
            tntOne = tnt[index]
            queueOne = deque[len(deque) - len(tnt) + index]

            if tntOne != queueOne:
                break
            index += 1

        if index == len(tnt): # 찾았으면 스택에서 제거
            for i in range(0, len(tnt)):
                deque.pop()

if len(deque) > 0:
    for ch in deque:
        print(ch, end='')
else:
    print("FRULA")