n = str(input("dime un palabra:"))
con = 0
print(len(n)//2)
for i in range (len(n)//2):
    if n[i]==n[-i-1]:
        con+=1
if con == (len(n)//2):
    print("es palindroma")
