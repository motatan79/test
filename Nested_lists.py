#Listas anidadas
lst = []

for i in range(int(input())):
    name = input()
    score = float(input())
    lst.append([name, score])
print(lst)
idx, min_value= min(lst, key=lambda x: x[1])
print(min_value)

lst3 = []
for i,j in lst:
    if j != min_value:
        lst3.append([i,j])

idx, min_value2 = min(lst3, key=lambda x: x[1])

lst4 = []
for i,j in lst3:
    if j == min_value2:
        lst4.append([i,j])

lst5 = []
for i in lst4:
    lst5.append(i[0])

sorted_list = sorted(lst5)

for i in sorted_list:
    print(i)