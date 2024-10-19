import math

polybius_square = {
    'A': 'PAHQG6', 'D': '4MEA1Y', 'F': 'L2NOFD', 'G': 'XKR3CV', 'V': 'S5ZW7B', 'X': '9UIT8J',
    'P': 'AA', 'H': 'AD', '0': 'AF', 'Q': 'AG', 'G': 'AV', '6': 'AX',
    '4': 'DA', 'M': 'DD', 'E': 'DF', 'A': 'DG', '1': 'DV', 'Y': 'DX',
    'L': 'FA', '2': 'FD', 'N': 'FF', 'O': 'FG', 'F': 'FV', 'D': 'FX',
    'X': 'GA', 'K': 'GD', 'R': 'GF', '3': 'GG', 'C': 'GV', 'V': 'GX',
    'S': 'VA', '5': 'VD', 'Z': 'VF', 'W': 'VG', '7': 'VV', 'B': 'VX',
    '9': 'XA', 'U': 'XD', 'I': 'XF', 'T': 'XG', '8': 'XV', 'J': 'XX'
}

def adfgvx_substitute(plaintext):
    plaintext = plaintext.upper()
    encoded_text = ''
    for char in plaintext:
        if char in polybius_square:
            encoded_text += polybius_square[char]
        else:
            raise ValueError(f"Character {char} not found in Polybius square.")
    return encoded_text

def columnar_transposition_encrypt(encoded_text, keyword):
    keyword_length = len(keyword)
    num_rows = math.ceil(len(encoded_text) / keyword_length)

    grid = [encoded_text[i * keyword_length:(i + 1) * keyword_length] for i in range(num_rows)]
    grid[-1] = grid[-1].ljust(keyword_length, '_')  # Pad the last row if necessary

    keyword_sorted = sorted(list(keyword))
    column_order = [keyword.index(char) for char in keyword_sorted]

    ciphertext = ''
    for idx in column_order:
        for row in grid:
            ciphertext += row[idx]

    return ciphertext

def adfgvx_cipher(plaintext, keyword):
    encoded_text = adfgvx_substitute(plaintext)
    ciphertext = columnar_transposition_encrypt(encoded_text, keyword)

    return ciphertext

if __name__ == "__main__":
    plaintext = "REDACTED"
    keyword = "KEYWORD"

    print(f"Plaintext: {plaintext}")
    ciphertext = adfgvx_cipher(plaintext, keyword)
    print(f"Ciphertext: {ciphertext}")
