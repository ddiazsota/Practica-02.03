Materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
n =[]
for i in Materias:
    nota = float(input(f"Cuanot has sacado en{i}:"))


    if nota>=5:
        n.append(i)


for i in n:
    Materias.remove(i)
print(Materias)
