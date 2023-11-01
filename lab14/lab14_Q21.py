from sys import getsizeof

a = 0.2
b = 0.1

c = a + b

print(c)
print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(c))

d = a - b

print(d)
print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(d))

e = a * b

print(e)
print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(e))

f = a / b

print(f)
print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(f))