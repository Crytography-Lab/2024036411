# ============================================================
#  Program 7: Double Columnar Transposition Cipher – Enc & Dec
# ============================================================

def get_order(key):
    """Return column reading order based on alphabetical key ranking."""
    indexed = sorted(enumerate(key.upper()), key=lambda x: x[1])
    order = [0] * len(key)
    for rank, (orig_idx, _) in enumerate(indexed):
        order[orig_idx] = rank
    return order


def columnar_encrypt(text, key):
    """Single-pass columnar transposition encrypt."""
    cols = len(key)
    # Pad with 'X' to fill the grid
    while len(text) % cols != 0:
        text += 'X'
    rows = len(text) // cols
    grid = [list(text[i*cols:(i+1)*cols]) for i in range(rows)]
    order = get_order(key)
    # Read columns in alphabetical key order
    col_order = sorted(range(cols), key=lambda c: order[c])
    ciphertext = ""
    for c in col_order:
        for r in range(rows):
            ciphertext += grid[r][c]
    return ciphertext


def columnar_decrypt(ciphertext, key):
    """Single-pass columnar transposition decrypt."""
    cols = len(key)
    rows = len(ciphertext) // cols
    order = get_order(key)
    col_order = sorted(range(cols), key=lambda c: order[c])
    # Fill columns back in
    grid = [[''] * cols for _ in range(rows)]
    idx = 0
    for c in col_order:
        for r in range(rows):
            grid[r][c] = ciphertext[idx]
            idx += 1
    return "".join("".join(row) for row in grid)


def double_columnar_encrypt(plaintext, key1, key2):
    """Apply columnar transposition twice (double columnar)."""
    step1 = columnar_encrypt(plaintext.upper().replace(" ", ""), key1)
    step2 = columnar_encrypt(step1, key2)
    return step2


def double_columnar_decrypt(ciphertext, key1, key2):
    """Reverse the double columnar transposition."""
    step1 = columnar_decrypt(ciphertext, key2)
    step2 = columnar_decrypt(step1, key1)
    return step2


def main():
    print("=" * 65)
    print("  DOUBLE COLUMNAR TRANSPOSITION – Encryption & Decryption")
    print("=" * 65)

    test_cases = [
        ("HELLO WORLD", "SECRET", "KEY"),
        ("ATTACK AT DAWN", "CRYPTO", "LOCK"),
        ("NETWORK SECURITY", "ALPHA", "BETA"),
        ("WE ARE DISCOVERED RUN", "ZEBRA", "MAGIC"),
    ]

    for i, (message, key1, key2) in enumerate(test_cases, 1):
        encrypted = double_columnar_encrypt(message, key1, key2)
        decrypted = double_columnar_decrypt(encrypted, key1, key2)
        print(f"\n--- Test Case {i} ---")
        print(f"  Plain Text  : {message}")
        print(f"  Key 1       : {key1}")
        print(f"  Key 2       : {key2}")
        print(f"  Encrypted   : {encrypted}")
        print(f"  Decrypted   : {decrypted}")
    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()
