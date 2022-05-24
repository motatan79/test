'''fh = open("romeo.txt", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")'''


n = 5
# Test one.
if n == 5:
    print('Yay!')

# Test two.
if n is 5:
    print('Yay!')


def es_primo(n):
    if n % 2 == 0:
        return "{n} es par".format(n)

es_primo(30)