# Para sumar los dígitos de numeros consecutivos
n = 2040
lista = []
suma = 0
while suma < 2040:
    for i in range(1,717):
        digits = len(str(i))
        lista.append(digits)
        suma = sum(lista)
print(suma)

numeros = []
for i in range(1, 717):
    numeros.append(i)
print(numeros[-1])