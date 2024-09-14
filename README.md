# RSA-Encryption-and-Decryption
This Python script implements a simple version of the RSA encryption algorithm. It demonstrates the generation of public and private keys, message encryption, and decryption using small prime numbers.

Description
RSA (Rivest–Shamir–Adleman) is a widely-used public-key cryptosystem. This script uses basic mathematical operations to illustrate the core concepts of RSA: generating public and private keys, encrypting a message, and decrypting it back to its original form.

In this code:
Two prime numbers p and q are used to generate the modulus n and the public key exponent e.
The public key (e, n) is used for encryption.
The private key d is used for decryption.
A message m is encrypted to C using the public key and then decrypted back to m using the private key.
This implementation is for educational purposes and should not be used for real encryption due to its simplicity and use of small primes.

To run the script, ensure that Python is installed on your system. The only external module used in the script is the built-in math module, which is part of the standard Python library.

Clone the Repository:
git clone https://github.com/yourusername/rsa_example.git
cd rsa_example

Requirements:
Python 3.x
Usage
To run the program, execute the script from your terminal or IDE.

Example Command:
python rsa_example.py

The script will:

Print the original message.
Encrypt the message and print the encrypted value.
Decrypt the message and print the decrypted value.
Functions
rsa_generate_Kpub(p, q)
Description: Generates the public key (e, n) from two prime numbers p and q.
Parameters:
p (int): First prime number.
q (int): Second prime number.
Returns: The public key components e and n.
rsa_generate_Kpriv(e, n)
Description: Generates possible private keys d using the public key (e, n).
Parameters:
e (int): Public key exponent.
n (int): Modulus from p * q.
Returns: A list of possible values for d.
rsa_encrypt(m, e, n)
Description: Encrypts a message m using the public key (e, n).
Parameters:
m (int): The original message.
e (int): Public key exponent.
n (int): Modulus from p * q.
Returns: The encrypted message C.
rsa_decrypt(c, d, n)
Description: Decrypts a ciphertext C using the private key d and modulus n.
Parameters:
C (int): The encrypted message (ciphertext).
d (int): Private key exponent.
n (int): Modulus from p * q.
Returns: The original message M.

Example
The following shows a basic example of the RSA process using the script:
p = 2
q = 7
n = p * q
e = 5
d = 11
msg = 5

# Encrypt message
C = rsa_encrypt(msg, e, n)

# Decrypt message
M = rsa_decrypt(C, d, n)

License
This project is licensed under the MIT License - see the LICENSE file for details.

