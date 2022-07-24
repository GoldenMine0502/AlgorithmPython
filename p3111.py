from collections import deque

A = input()
T = input()

deque = deque()
# right = deque()


def checkLast(text, queue):
    if len(queue) >= len(text):
        for i in range(0, len(text)):
            textOne = text[i]
            queueOne = queue[len(queue) - len(text) + i]

            if textOne != queueOne:
                return False
        return True
    return False


mode = True  # True이면 그대로, False이면 반대로

leftIndex = 0
rightIndex = len(T) - 1

while True:
    if mode:
        deque.append(T[leftIndex])

        censor = True

        if len(deque) >= len(A):
            for i in range(0, len(A)):
                textOne = A[i]
                queueOne = deque[len(deque) - len(deque) + i]

                if textOne != queueOne:
                    censor = False
                    break

        if leftIndex == rightIndex:
            break

        leftIndex += 1
    else:
        deque.append(T[rightIndex])

        if leftIndex == rightIndex:
            break

        leftIndex -= 1
    # one = T[leftIndex] if mode else T[rightIndex]
    #
    # deque.append(one)
    #
    # if checkLast(A, deque):
    #     for j in range(0, len(A)):
    #         deque.pop()
    #
    #     mode = not mode

    if leftIndex == rightIndex:
        break

    if mode:
        leftIndex += 1
    else:
        rightIndex -= 1
# for i in range(0, len(left)):
#     print(left[i], end='')
#
# for i in range(0, len(right)):
#     print(right[i], end='')


print(left)
print(right)