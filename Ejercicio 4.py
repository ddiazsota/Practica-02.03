print("Dime los numero ganadores de la primitiva:")
i = "Si"
lista_primi = []
while i!="No" and i!="no" and i!="NO":


    n_primitiva = int(input(":"))
    print("Hay mas numeros ganadores:")
    lista_primi.append(n_primitiva)
    i = input("Si/No:")
lista_primi.sort()
print(lista_primi)
