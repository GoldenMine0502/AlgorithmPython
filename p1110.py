def convert(number):
    digit1 = number // 10
    digit0 = number - digit1 * 10

    return digit0 * 10 + (digit0 + digit1) % 10


start = int(input())

count = 0
number = start

while count == 0 or start != number:
    # print(number)
    number = convert(number)
    count += 1

print(count)