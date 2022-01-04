import random
x = input("Enter a word : ")
x = list(x)
l = []
y = ""
while len(l) != len(x):
    r = random.randint(0, len(x) - 1)
    if r not in l:
        l.append(r)
for i in l:
    y += x[i]
print(y)