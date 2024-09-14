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

Print the original message, encrypt the message, and print the encrypted value, followed by decrypting the message and printing the decrypted value. The function rsa_generate_Kpub(p, q) generates the public key (e, n) from two prime numbers p and q. The parameters for this function include p (the first prime number) and q (the second prime number), and it returns the public key components e and n. The function rsa_generate_Kpriv(e, n) generates possible private keys d using the public key (e, n). The parameters for this function are e (the public key exponent) and n (the modulus, calculated as p * q), and it returns a list of possible values for d. The function rsa_encrypt(m, e, n) encrypts a message m using the public key (e, n). The parameters for this function are m (the original message), e (the public key exponent), and n (the modulus from p * q), and it returns the encrypted message C. The function rsa_decrypt(c, d, n) decrypts a ciphertext C using the private key d and modulus n. The parameters for this function include C (the encrypted message or ciphertext), d (the private key exponent), and n (the modulus from p * q), and it returns the original message M. For example, the following shows a basic example of the RSA process using the script: p = 2, q = 7, n = p * q, e = 5, d = 11, and msg = 5.

# Encrypt message
C = rsa_encrypt(msg, e, n)

# Decrypt message
M = rsa_decrypt(C, d, n)

License
This project is licensed under the MIT License - see the LICENSE file for details.

