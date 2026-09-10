# ============================================================
#  Program 5: Playfair Cipher – Encryption & Decryption
# ============================================================

def generate_playfair_matrix(key):
    """Generate a 5x5 Playfair key matrix from the given key."""
    key = key.upper().replace("J", "I")
    seen = []
    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.append(ch)
    return [seen[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, ch):
    for r, row in enumerate(matrix):
        if ch in row:
            return r, row.index(ch)
    return None


def prepare_text(text):
    """Prepare plaintext: uppercase, replace J→I, insert X between digraphs."""
    text = text.upper().replace("J", "I").replace(" ", "")
    result = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            result.append((a, 'X'))
            i += 1
        else:
            result.append((a, b))
            i += 2
    if len(result[-1][1]) == 0 or (result and result[-1][1] == ''):
        last = result[-1]
        result[-1] = (last[0], 'X')
    return result


def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    pairs = prepare_text(plaintext)
    ciphertext = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            ciphertext += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            ciphertext += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
    return ciphertext


def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    pairs = [(ciphertext[i], ciphertext[i+1]) for i in range(0, len(ciphertext), 2)]
    plaintext = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    return plaintext


def main():
    print("=" * 60)
    print("       PLAYFAIR CIPHER – Encryption & Decryption")
    print("=" * 60)

    test_cases = [
        ("HELLO", "KEYWORD"),
        ("MEET ME", "MONARCHY"),
        ("HIDE GOLD", "PLAYFAIR"),
        ("ATTACK NOW", "SECRET"),
    ]

    for i, (message, key) in enumerate(test_cases, 1):
        encrypted = playfair_encrypt(message, key)
        decrypted = playfair_decrypt(encrypted, key)
        print(f"\n--- Test Case {i} ---")
        print(f"  Plain Text  : {message}")
        print(f"  Key         : {key}")
        print(f"  Encrypted   : {encrypted}")
        print(f"  Decrypted   : {decrypted}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
