cipher = {'A': { 'A':'M', 'D': 'S', 'F':'T', 'G': 'P', 'V': 'Z', 'X':'E'},
          'D': { 'A':'R', 'D': 'F', 'F':'B', 'G': 'L', 'V': '9', 'X':'V'},
          'F': { 'A':'D', 'D': 'G', 'F':'Y', 'G': 'U', 'V': '8', 'X':'I'},
          'G': { 'A':'J', 'D': 'O', 'F':'K', 'G': 'H', 'V': '7', 'X':'W'},
          'V': { 'A':'{', 'D': '}', 'F':'3', 'G': '4', 'V': '0', 'X':'_'},
          'X': { 'A':'N', 'D': 'A', 'F':'X', 'G': 'C', 'V': '5', 'X':'Q'}}

flag = "REDACTED"

def get_pair(c : str) -> str:
    for i in cipher:
        for j in cipher:
            if cipher[i][j] == c:
                return i+j
    raise Exception(f"Invalid sequence {c} entered")

enc = "".join([get_pair(i) for i in flag])
print(enc)
