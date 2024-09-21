text = input()

text = text.replace("c=", "1")
text = text.replace("c-", "1")
text = text.replace("dz=", "1")
text = text.replace("d-", "1")
text = text.replace("lj", "1")
text = text.replace("nj", "1")
text = text.replace("s=", "1")
text = text.replace("z=", "1")

# text = text.replace("lj", "g")
# ljlj -> gg -> 2
# eljlj -> egg -> 3

# print(text)
print(len(text))