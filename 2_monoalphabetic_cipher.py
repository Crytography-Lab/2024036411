# ============================================================
#  Program 2: Monoalphabetic Cipher – Encryption & Decryption
# ============================================================

ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CIPHER_KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"  # Fixed substitution key


def mono_encrypt(plaintext):
    """Encrypt plaintext using a monoalphabetic substitution cipher."""
    result = ""
    for ch in plaintext.upper():
        if ch in ALPHABET:
            result += CIPHER_KEY[ALPHABET.index(ch)]
        else:
            result += ch
    return result


def mono_decrypt(ciphertext):
    """Decrypt ciphertext using the reverse substitution key."""
    result = ""
    for ch in ciphertext.upper():
        if ch in CIPHER_KEY:
            result += ALPHABET[CIPHER_KEY.index(ch)]
        else:
            result += ch
    return result


def main():
    print("=" * 60)
    print("    MONOALPHABETIC CIPHER – Encryption & Decryption")
    print("=" * 60)
    print(f"  Substitution Key : {CIPHER_KEY}")

    test_cases = [
        "HELLO WORLD",
        "ATTACK AT DAWN",
        "NETWORK SECURITY",
        "CRYPTOGRAPHY IS FUN",
    ]

    for i, message in enumerate(test_cases, 1):
        encrypted = mono_encrypt(message)
        decrypted = mono_decrypt(encrypted)
        print(f"\n--- Test Case {i} ---")
        print(f"  Plain Text  : {message}")
        print(f"  Encrypted   : {encrypted}")
        print(f"  Decrypted   : {decrypted}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
