abcedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n=[]
for i in abcedario:
    if (abcedario.index(i)+1) % 3 == 0:
        n.append(i)
for i in n:
    abcedario.remove(i)
print(abcedario)


