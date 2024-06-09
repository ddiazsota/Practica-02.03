lista = [1,2,3,4,5,6,7,8,9,10]
lista.sort(reverse=True)
a = ""
for i in lista:
    if i!=lista[9]:
        a = a+f"{i}"+","
    else:
        a = a+f"{i}"
print(a)
