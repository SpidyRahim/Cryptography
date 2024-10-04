import random
from math import gcd

# Function to compute modular inverse
def mod_inverse(e, phi):
    # Extended Euclidean Algorithm
    d = 0
    x1, x2, x3 = 0, 1, phi
    y1, y2, y3 = 1, 0, e
    while y3 != 0:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    if x2 < 0:
        x2 += phi
    return x2

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a random prime number
def generate_prime(start, end):
    primes = [i for i in range(start, end) if is_prime(i)]
    return random.choice(primes)

# Key generation
def generate_keys():
    # Choose two random prime numbers
    p = generate_prime(100, 300)
    q = generate_prime(100, 300)

    n = p * q  # Modulus for public and private keys
    phi = (p - 1) * (q - 1)  # Euler's Totient Function

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Compute the modular inverse of e mod phi, which is d
    d = mod_inverse(e, phi)

    # Public key (e, n) and Private key (d, n)
    return ((e, n), (d, n))

# Encryption: C = M^e mod n
def encrypt(plain_text, public_key):
    e, n = public_key
    cipher_text = [(ord(char) ** e) % n for char in plain_text]
    return cipher_text

# Decryption: M = C^d mod n
def decrypt(cipher_text, private_key):
    d, n = private_key
    plain_text = [chr((char ** d) % n) for char in cipher_text]
    return ''.join(plain_text)

# Main Program
if __name__ == "__main__":
    print("Generating RSA keys...")
    public_key, private_key = generate_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = input("\nEnter a message to encrypt: ")
    
    # Encrypt the message
    encrypted_msg = encrypt(message, public_key)
    print("\nEncrypted message:", encrypted_msg)

    # Decrypt the message
    decrypted_msg = decrypt(encrypted_msg, private_key)
    print("Decrypted message:", decrypted_msg)
