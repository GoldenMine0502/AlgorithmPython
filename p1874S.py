
# 값 입력 부분

N = int(input())

inputs = []

for i in range(0, N):
    inputs.append(int(input()))

# 스택 계산 부분

stack = []  # 문제를 풀기 위한 스택
result = []  # 결과 출력용 배열
count = 1  # 지금까지 넣은 값

succeed = True  # 성공, 실패여부(NO)

for i in range(0, N):
    value = inputs[i]

    while count <= value:
        # 스택 추가
        stack.append(count)
        result.append("+")
        count = count + 1

    # 스택 제거
    if value == stack[-1]:
        stack.pop()
        result.append("-")
    else:
        succeed = False
        break

# 결과 출력 부분

if succeed:
    for i in range(0, len(result)):
        print(result[i])
else:
    print("NO")
