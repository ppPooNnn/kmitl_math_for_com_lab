import sympy as sp
import numpy as np

def finde(phin):
    e = 2
    while True:
        if sp.gcd(phin, e) == 1:
            break
        e += 1
    return e

def findd(e, phin):
    d = 1
    while True:
        if (d * e) % phin == 1:
            break
        d += 1
    return d

def encrypt(M, e, n):
    C = pow(M, e, n)  # Use pow function with three arguments for efficient modular exponentiation
    return C

def decrypt(C, d, n):
    M = pow(C, d, n)  # Use pow function with three arguments for efficient modular exponentiation
    return M

p = sp.randprime(1, 100)
q = sp.randprime(1, 100)
n = p * q
phin = (p - 1) * (q - 1)
e = finde(phin)
d = findd(e, phin)
allkey = [[e, n], [d, n]]

print("Public Key is:", allkey[0])
print("Private Key is:", allkey[1])
print("My student Code is 66050067")
code = encrypt("66050067", e, n)
print("Ciphertext message is:", code)
print("The decrypted message is:", decrypt(code, d, n))
