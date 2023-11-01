import random
import math
# import numpy as np
import sympy

primes = [i for i in range(2,100) if sympy.isprime(i)]
p = random.choice(primes)
q = random.choice(primes)

n = p * q
phi_n = (p - 1) * (q - 1)
e = 2
while math.gcd(e,phi_n) != 1 :
    e += 1
d = 1
while (d * e) % phi_n != 1 :
    d += 1

def encrypt(M) :
    C = pow(M, e, n)
    return C

def decrypt(C, d, n) :
    M = pow(C, d, n)
    return M

def main() :
    Message = "donutchobkinkongwhan"
    Decrypt_Message = ''
    Encrypt_Message = ''
    for Char in Message : 
        M1 = ord(Char)
        C1 = encrypt(M1)
        Encrypt_Message += chr(int(C1))
    print('public key are e =', e, 'and n =', n)
    print('private key are d =', d, 'and n =', n)
    print('\n---------------------Encrypting---------------------------------')
    print('this is Message to encrypt =', Message)
    print('this is Message after encrypt =', Encrypt_Message)
    for Char in Encrypt_Message :
        C2 = ord(Char)
        M2 = decrypt(C2, d, n)
        Decrypt_Message += chr(int(M2))
    print('---------------------Decrypting--------------------------------')
    print('this is Message to decrypt =', Encrypt_Message)
    print('this is Message after decrypt', Decrypt_Message)
    print('---------------------------------------------------------------')

if __name__ == "__main__" :
    main()