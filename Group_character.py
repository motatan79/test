import re
a = '..12345678910111213141516171820212223'
print(type(a))
numbers = re.findall(r'[0-9]+', a)
print(type(numbers))
s = "".join([str(_) for _ in numbers])
x = [int(a) for a in str(s)]
print(x)

x2 = []
for i in x:
    if i not in x2:
        x2.append(i)
print(x2)

for i in x2:
    e = x.count(i)
    print(i,e)