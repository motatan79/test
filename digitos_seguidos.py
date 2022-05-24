# Para dar como resultado los digitos seguidos de una secuencia de numeros
n = int(input('Agregue un numero: '))
a = []
for i in range(1, n+1):
    a.append(i)
print(''.join(map(str, a)))