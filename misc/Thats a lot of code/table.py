
    plaintext = "REDACTED"
    for char in plaintext:
    ciphertext = ''
    keyword_length = len(keyword)
          'F': { 'A':'D', 'D': 'G', 'F':'Y', 'G': 'U', 'V': '8', 'X':'I'},
        for row in grid:


    keyword_sorted = sorted(list(keyword))
    print(f"Plaintext: {plaintext}")
    grid[-1] = grid[-1].ljust(keyword_length, '_')  # Pad the last row if necessary
    return encoded_text
    ciphertext = adfgvx_cipher(plaintext, keyword)
    keyword = "KEYWORD"
        if char in polybius_square:
    for i in cipher:
            encoded_text += polybius_square[char]
          'X': { 'A':'N', 'D': 'A', 'F':'X', 'G': 'C', 'V': '5', 'X':'Q'}}
          'G': { 'A':'J', 'D': 'O', 'F':'K', 'G': 'H', 'V': '7', 'X':'W'},
    'P': 'AA', 'H': 'AD', '0': 'AF', 'Q': 'AG', 'G': 'AV', '6': 'AX',
            ciphertext += row[idx]
def columnar_transposition_encrypt(encoded_text, keyword):




    plaintext = plaintext.upper()

def adfgvx_cipher(plaintext, keyword):
    'S': 'VA', '5': 'VD', 'Z': 'VF', 'W': 'VG', '7': 'VV', 'B': 'VX',
    for idx in column_order:
        else:
    num_rows = math.ceil(len(encoded_text) / keyword_length)
}
    'A': 'PAHQG6', 'D': '4MEA1Y', 'F': 'L2NOFD', 'G': 'XKR3CV', 'V': 'S5ZW7B', 'X': '9UIT8J',
import math
    print(f"Ciphertext: {ciphertext}")
print(enc)
          'D': { 'A':'R', 'D': 'F', 'F':'B', 'G': 'L', 'V': '9', 'X':'V'},
polybius_square = {
    return ciphertext
    'X': 'GA', 'K': 'GD', 'R': 'GF', '3': 'GG', 'C': 'GV', 'V': 'GX',
    grid = [encoded_text[i * keyword_length:(i + 1) * keyword_length] for i in range(num_rows)]

    return ciphertext

    '4': 'DA', 'M': 'DD', 'E': 'DF', 'A': 'DG', '1': 'DV', 'Y': 'DX',
    column_order = [keyword.index(char) for char in keyword_sorted]
    encoded_text = ''
flag = "REDACTED"
def get_pair(c : str) -> str:
    'L': 'FA', '2': 'FD', 'N': 'FF', 'O': 'FG', 'F': 'FV', 'D': 'FX',
        for j in cipher:

enc = "".join([get_pair(i) for i in flag])
    encoded_text = adfgvx_substitute(plaintext)
    '9': 'XA', 'U': 'XD', 'I': 'XF', 'T': 'XG', '8': 'XV', 'J': 'XX'

if __name__ == "__main__":
def adfgvx_substitute(plaintext):
            raise ValueError(f"Character {char} not found in Polybius square.")
          'V': { 'A':'{', 'D': '}', 'F':'3', 'G': '4', 'V': '0', 'X':'_'},
    raise Exception(f"Invalid sequence {c} entered")
            if cipher[i][j] == c:
cipher = {'A': { 'A':'M', 'D': 'S', 'F':'T', 'G': 'P', 'V': 'Z', 'X':'E'},

                return i+j

    ciphertext = columnar_transposition_encrypt(encoded_text, keyword)
