# Hill Cipher with Hash Function

A Python implementation of a 3x3 Hill Cipher combined with a bitwise hash function. Encryption and Decryption Matrices have been hardcoded.

## Features

* **Classical Encryption:** Utilizes a 3x3 matrix-based Hill Cipher to encrypt messages in blocks of three characters.
* **Integrity Verification:** Generates a 3-character (32-bit) Message Authentication Code (MAC) using custom bitwise operations (XOR and bit-shifting) bound to a secret key.
* **Auto-Formatting:** Automatically strips non-alphabetic characters, converts text to uppercase, and pads the payload with `X` to fit the required block size.

## Prerequisites

* Python 3.x
* NumPy (`pip install numpy`)

## Usage

1. Run the script from your terminal:
   ```bash
   python hill_cipher_auth.py
   ```
2. Enter your plaintext message when prompted (spaces and punctuation will be ignored).
3. Enter a secret key for the hash generation.
4. The script will output the combined payload (message + hash + padding), the encrypted ciphertext, the decrypted plaintext, and the integrity verification status.
