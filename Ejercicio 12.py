import statistics
lista = input("dimme una lista de numero separada por comas:")
c = lista.split(",")
lista_2 = list(map(int, c))


tipica=statistics.pstdev(lista_2)
print(tipica)
