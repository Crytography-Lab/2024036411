# ============================================================
#  Program 3: Polyalphabetic (Vigenère) Cipher – Enc & Dec
# ============================================================

def vigenere_encrypt(plaintext, key):
    """Encrypt plaintext using the Vigenère cipher."""
    ciphertext = ""
    key = key.upper()
    key_index = 0
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            ciphertext += chr((ord(ch) - base + shift) % 26 + base)
            key_index += 1
        else:
            ciphertext += ch
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    """Decrypt ciphertext using the Vigenère cipher."""
    plaintext = ""
    key = key.upper()
    key_index = 0
    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            plaintext += chr((ord(ch) - base - shift) % 26 + base)
            key_index += 1
        else:
            plaintext += ch
    return plaintext


def main():
    print("=" * 60)
    print("  POLYALPHABETIC (VIGENÈRE) CIPHER – Enc & Dec")
    print("=" * 60)

    test_cases = [
        ("HELLO WORLD", "KEY"),
        ("ATTACK AT DAWN", "LEMON"),
        ("NETWORK SECURITY", "CRYPTO"),
        ("PYTHON IS AMAZING", "SECRET"),
    ]

    for i, (message, key) in enumerate(test_cases, 1):
        encrypted = vigenere_encrypt(message, key)
        decrypted = vigenere_decrypt(encrypted, key)
        print(f"\n--- Test Case {i} ---")
        print(f"  Plain Text  : {message}")
        print(f"  Key         : {key}")
        print(f"  Encrypted   : {encrypted}")
        print(f"  Decrypted   : {decrypted}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
