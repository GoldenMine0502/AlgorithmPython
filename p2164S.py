from collections import deque

N = int(input())

queue = deque()
# deque([_ for _ in range(1, N + 1)])

for i in range(0, N):
    queue.append(i + 1)

mode = True

while len(queue) > 1:  # 크기가 1이 될 때 까지 반복
    if mode:  # True인 경우 앞 제거
        queue.popleft()
        mode = False
    else:  # False인 경우 뒤로 보내기
        value = queue.popleft()
        queue.append(value)
        mode = True

print(queue.pop())  # popleft()를 하던 pop()을 하던 상관없다
