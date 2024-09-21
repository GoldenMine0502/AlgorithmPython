N = int(input())

for i in range(N):
    a, text = input().split()
    count = int(a)

    result = ""

    for ch in text:
        for j in range(count):
            result += ch

    print(result)


# text = "abcdef"

# for ch in text:
#     print(ch)

# for i in range(len(text)):
#     print(text[i])
