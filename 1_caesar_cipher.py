# ============================================================
#  Program 1: Caesar Cipher – Encryption & Decryption
# ============================================================

def caesar_encrypt(plaintext, shift):
    """Encrypt plaintext using Caesar Cipher with the given shift."""
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            ciphertext += chr((ord(ch) - base + shift) % 26 + base)
        else:
            ciphertext += ch
    return ciphertext


def caesar_decrypt(ciphertext, shift):
    """Decrypt ciphertext using Caesar Cipher with the given shift."""
    return caesar_encrypt(ciphertext, -shift)


def main():
    print("=" * 55)
    print("         CAESAR CIPHER – Encryption & Decryption")
    print("=" * 55)

    test_cases = [
        ("HELLO WORLD", 3),
        ("ATTACK AT DAWN", 13),
        ("Python Programming", 7),
        ("NetworkSecurity2024!", 17),
    ]

    for i, (message, key) in enumerate(test_cases, 1):
        encrypted = caesar_encrypt(message, key)
        decrypted = caesar_decrypt(encrypted, key)
        print(f"\n--- Test Case {i} ---")
        print(f"  Plain Text  : {message}")
        print(f"  Shift (Key) : {key}")
        print(f"  Encrypted   : {encrypted}")
        print(f"  Decrypted   : {decrypted}")
    print("\n" + "=" * 55)


if __name__ == "__main__":
    main()
