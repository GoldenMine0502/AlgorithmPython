text = input()

arr = []

for i in range(26):
    arr.append(0)

for i in range(len(text)):
    ch = text[i]

    if 'A' <= ch <= 'Z':
        index = ord(ch) - ord('A')
        arr[index] += 1
    else:  # 이 경우는 소문자
        index = ord(ch) - ord('a')
        arr[index] += 1

maxCount = 0
max = 0
maxIndex = 0

for i in range(26):
    count = arr[i]

    if count > max:
        max = count  # -> count == max -> true
        maxIndex = i
        maxCount = 1
    elif count == max:
        maxCount += 1

# print(maxCount, max, maxIndex)

if maxCount == 1:
    print(chr(maxIndex + ord('A')))
else:
    print("?")
