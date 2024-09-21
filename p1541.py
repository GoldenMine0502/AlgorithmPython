text = input()

arr = []
temp = ""

# 10+20-30
# -1
# 첫 음수 위치
firstMinusPosition = -1

for i in range(0, len(text)):
    if text[i] == '+' or text[i] == '-':
        arr.append(temp)

        if text[i] == '-' and firstMinusPosition == -1:
            firstMinusPosition = len(arr)

        temp = ""
    else:
        temp += text[i]

    # print(text[i], temp)

if len(temp) > 0:
    arr.append(temp)

# print(arr)

sum = 0

if firstMinusPosition == -1:
    for i in range(0, len(arr)):
        sum += int(arr[i])
else:
    for i in range(0, len(arr)):
        number = int(arr[i])

        # print(number, i, firstMinusPosition)

        if i >= firstMinusPosition:
            sum -= number
        else:
            sum += number

print(sum)