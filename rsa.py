import math

# Generate public key (e, n) using two large prime numbers p and q
def rsa_generate_Kpub(p, q):
    n = p*q
    print("n =", n)
    
    phi_n = (p-1)*(q-1)
    
    e = 2
    while(e<phi):
        if (math.gcd(e, phi) == 1):
            break
        else:
            e += 1
    print("e =", e)
    
    return e, n

# Generate private key using public key (e, n)
def rsa_generate_Kpriv(e, n):
    l = []
    tmp = 1
    while len(l) <= 5:
        if (tmp *e) % phi == 1:
            l.append(tmp)
        tmp += 1

    print("5 possible d values: ", l)
    return l

# Encrypt message m using public key (e, n)
def rsa_encrypt(m, e, n):
    C = (m**e) % n
    print(f'Encrypted message: {C}')
    return C
    
# Decrypt ciphertext C using private key d, and n
def rsa_decrypt(c, d, n):
    M = (c**d) % n
    print(f'Decrypted message: {M}')
    return M


# Example
p = 2
q = 7

n = p*q # n = pq -> ALWAYS

e = 5 # public key
d = 11 # private key

msg = 5
print(f'original message: {msg}')

C = rsa_encrypt(msg, e, n); # Get ciphertext C
M = rsa_decrypt(C, d, n); # Get decrypted message M