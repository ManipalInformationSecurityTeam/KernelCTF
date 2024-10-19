## A glitch in the matrix
The sequence of numbers—81, 64, 64, 65, 64, 75, 66, 83, 78, 93, 77, 74, 68, 73, 78, 78, 72, 72, 80, 82, 85, 86, 86, 93, 94, 53, 55, 52, 50, 50, 55, 51, 49, 57, 59, 93—may seem random at first glance, but conceals deeper meanings when examined exclusively as part of a broader scheme.
EWKXJCMER0VCDE
Provide: [wheatstone.txt](wheatstone.txt)

### HINT
Two grids in a room, they might ____<br>
All results as strings <br>

### Solution
You have to convert the numbers into a 6x6 matrix, then xor individually w the numbers in the ciphertext(Base64). Convert every xored number to ascii, combine and get a string (or basically the playfair grid). Tihs will give you the playfair grid
Then playfair decode the grid and the string, giving you the flag. (ANOTSOFAIRPLAY)
`wtfCTF{ANOTSOFAIRPLAY}`