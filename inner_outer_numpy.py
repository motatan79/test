import numpy as np

a = np.array([0, 1])
b = np.array([3, 4])

print(np.inner(a,b))

A = np.array(input().split( ), int)
B = np.array(input().split( ), int)
print(np.inner(A,B))
print(np.outer(A,B))

