## Question
Hehe, I've hid a 15 character massive file. It's unlikely you're ever finding it

*[dump.txt]*

Wrap the flag in the format wtfCTF{flag-here}

## Hints

1) There's no pattern to the way the letters are arranged, but there's a trend

2) No matter how big the file is, it's the content that *counts*

3) The flag is in ascending order


## Solution
The file is filled with alphanumeric characters(a-z, A-Z and 0-9), the file is too big to prune through manually

If you'd try to get some statistics on the characters, you'll see that each has a different frequency. Sorting these charachters by frequency(Or plotting them), you'll see that the first 15 characters spell the flag

['F', 'r', '3', 'q', 'u', 'e', 'n', 'C', 'y', 'd', '0', 'm', 'a', '1', 'N', 'z', 'X', 'Q', 'P', 'k', 'Z', 'f', 'H', 'J', 's', 'j', 'B', '5', 't', 'M', 'V', 'o', 'L', 'w', 'D', '4', '8', 'A', 'U', '9', 'l', 'c', 'g', '7', 'p', 'O', 'T', 'h', 'x', 'K', 'v', 'G', 'W', '2', 'b', 'I', 'S', '6', 'i', 'R', 'Y', 'E']

Fr3qenCyd0ma1Nz
wrap that in wtfCTF{}: wtfCTF{Fr3qenCyd0ma1Nz}