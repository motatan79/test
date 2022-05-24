# Elegir segundo numero más alto
arr = [2, 3, 6, 6, 5, 7]
lista2 = []
for i in arr:
    if i not in lista2:
        lista2.append(i)
a = (max(lista2))
lista2.remove(a)
lista3 = sorted(lista2)
print(lista3[-1])