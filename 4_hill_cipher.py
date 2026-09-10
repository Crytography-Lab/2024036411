# ============================================================
#  Program 4: Hill Cipher – Encryption & Decryption
# ============================================================

def mat_mul_mod(A, v, m=26):
    """Multiply 2x2 matrix A by vector v under mod m."""
    return [(A[0][0]*v[0] + A[0][1]*v[1]) % m,
            (A[1][0]*v[0] + A[1][1]*v[1]) % m]


def mod_inv(a, m=26):
    """Find modular multiplicative inverse of a under mod m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def mat_inv_2x2(K, m=26):
    """Compute modular inverse of a 2x2 matrix."""
    det = (K[0][0]*K[1][1] - K[0][1]*K[1][0]) % m
    di = mod_inv(det, m)
    return [[di * K[1][1] % m,  (-di * K[0][1]) % m],
            [(-di * K[1][0]) % m, di * K[0][0] % m]]


def hill_encrypt(text, K=[[3, 3], [2, 5]]):
    """Encrypt plaintext using the Hill cipher."""
    t = text.upper().replace(" ", "")
    if len(t) % 2:
        t += 'X'
    out = ""
    for i in range(0, len(t), 2):
        v = [ord(t[i]) - 65, ord(t[i+1]) - 65]
        r = mat_mul_mod(K, v)
        out += chr(r[0] + 65) + chr(r[1] + 65)
    return out


def hill_decrypt(text, K=[[3, 3], [2, 5]]):
    """Decrypt ciphertext using the inverse Hill matrix."""
    IK = mat_inv_2x2(K)
    out = ""
    for i in range(0, len(text), 2):
        v = [ord(text[i]) - 65, ord(text[i+1]) - 65]
        r = mat_mul_mod(IK, v)
        out += chr(r[0] + 65) + chr(r[1] + 65)
    return out


def main():
    print("=" * 60)
    print("         HILL CIPHER - Encryption & Decryption")
    print("=" * 60)
    print("\n  Key Matrix : [[3, 3], [2, 5]]")

    test_cases = ["HELP", "MATH", "PYTHON", "NETWORK"]
    for i, message in enumerate(test_cases, 1):
        encrypted = hill_encrypt(message)
        decrypted = hill_decrypt(encrypted)
        print(f"\n--- Test Case {i} ---")
        print(f"  Plain Text  : {message}")
        print(f"  Encrypted   : {encrypted}")
        print(f"  Decrypted   : {decrypted}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
