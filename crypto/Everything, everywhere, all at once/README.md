## Everything, everywhere, all at once
In a world filled with chaos and disorder, can you decipher the underlying patterns that bring clarity?  <br>

Provided files: [ciphertext1.txt](ciphertext.txt)
[ciphertext2.txt](ciphertext2.txt)

### HINT
I once ate like 256 hashbrowns in one sitting :o <br>
Only numbers remain
### SOLUTION
You have to decrypt ciphertext1 w chaocipher to get part of the flag **wtfCTF{AVALANCHE_EFFECT**<br>
![Screenshot 2024-10-15 214445](https://github.com/user-attachments/assets/0fa0f33c-6e23-4eed-8223-1e6ffdd2c773)
<br>
then, you have to hash this part, concatenated with a random 6 digit number + "}", such that its hash will match the hash of the flag(in ciphertext2) <br>
the flag is `wtfCTF{AVALANCHE_EFFECT_897659}`