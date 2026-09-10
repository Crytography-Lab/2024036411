# ============================================================
#  Program 6: Rail Fence Cipher – Encryption & Decryption
# ============================================================

def rail_fence_encrypt(plaintext, rails):
    """Encrypt using the Rail Fence (Zigzag) transposition cipher."""
    fence = [[] for _ in range(rails)]
    rail, direction = 0, 1
    for ch in plaintext:
        fence[rail].append(ch)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return "".join("".join(r) for r in fence)


def rail_fence_decrypt(ciphertext, rails):
    """Decrypt a Rail Fence ciphertext."""
    n = len(ciphertext)
    pattern = []
    rail, direction = 0, 1
    for i in range(n):
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    indices = sorted(range(n), key=lambda i: pattern[i])
    result = [''] * n
    for i, idx in enumerate(indices):
        result[idx] = ciphertext[i]
    return "".join(result)


def main():
    print("=" * 60)
    print("      RAIL FENCE CIPHER – Encryption & Decryption")
    print("=" * 60)

    test_cases = [
        ("HELLO WORLD", 3),
        ("ATTACK AT DAWN", 2),
        ("WEAREDISCOVEREDRUNATONCE", 3),
        ("NETWORK SECURITY IS KEY", 4),
    ]

    for i, (message, rails) in enumerate(test_cases, 1):
        encrypted = rail_fence_encrypt(message, rails)
        decrypted = rail_fence_decrypt(encrypted, rails)
        print(f"\n--- Test Case {i} ---")
        print(f"  Plain Text  : {message}")
        print(f"  Rails       : {rails}")
        print(f"  Encrypted   : {encrypted}")
        print(f"  Decrypted   : {decrypted}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
