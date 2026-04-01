import numpy as np

M1 = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
M2 = np.array([[8, 5, 10], [21, 8, 21], [21, 12, 8]])

def hash(msg, key):
    h_val = 0
    for i, char in enumerate(msg + key):
        h_val = ((h_val << 4) ^ (h_val >> 28) ^ ord(char) ^ i) & 0xFFFFFFFF
    
    c1 = chr((h_val % 26) + 65)
    c2 = chr(((h_val >> 8) % 26) + 65)
    c3 = chr(((h_val >> 16) % 26) + 65)
    return c1 + c2 + c3

def run_hill(txt, m):
    out = ""
    for i in range(0, len(txt), 3):
        block = [ord(c) - 65 for c in txt[i:i+3]]
        res = np.dot(m, np.array(block)) % 26
        out += "".join(chr(int(n) + 65) for n in res)
    return out

if __name__ == "__main__":
    raw_in = input("Enter message: ")
    secret = input("Enter secret key: ")

    clean = "".join(c.upper() for c in raw_in if c.isalpha())
    
    mac = hash(clean, secret)
    payload = clean + mac
    
    while len(payload) % 3 != 0:
        payload += 'X'

    print(f"\nCombined Payload: {payload}")
    
    c_text = run_hill(payload, M1)
    print(f"Ciphertext: {c_text}")

    p_text = run_hill(c_text, M2)
    print(f"Decrypted: {p_text}")

    xtr_msg = p_text[:len(clean)]
    xtr_hash = p_text[len(clean):len(clean)+3]

    if hash(xtr_msg, secret) == xtr_hash:
        print("Integrity Verified")
    else:
        print("Message Tampered")
