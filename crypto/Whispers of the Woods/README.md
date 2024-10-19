## Whispers of the Woods
In a quiet forest, a LITTLE rabbit came across a peculiar scene. An ancient typewriter sat beneath a large tree. The typewriter displayed an odd sequence of characters: <br>
*949d407e5e298705f96a81816a084778c000adc2e933* <br>
Beside it, a locked box bore the inscription "key". Inside the keyhole, it discovered a small slip of paper with a lengthy string:<br>
"S62N02837469V4912570SV5861694890"<br>
As it inspected the typewriter, an duck waddled up, quacking:<br>
"Naknak Nanak Nanananak Nak? Nanananak Nananak Naknak Nanananak Naknak Nanananak Naknak Naknak Nanananak Naknaknak Naknak Nanak Naknak Nak? Naknak nak? Naknak Nanananak Naknak Nanananak Nanananak Nananak Nanananak Nanak Naknak Nanak Nanananak Nak."<br>
### HINT 
"SHIFT your understanding, and with one RIGHT touch, the key will make sense. But not everything fits where it should. What seems like nonsense INITIALLY, may hold the answer to something else." <br>
theres a jungle, a little rabbit moves to the right, and crashes into the duck.

### SOLUTION
The typewriter message is the input for RABBIT cipher. This cypher uses a 128bit key, that we have encrypted using keyboard shift to the right (by 1), and a 64bit IV (Initialization Vector), which we encoded using a naknak duck cipher (on dcode). <br>
Using the hints we need to first decode the key and IV. Put those values in their positions with the token you get the flag that is
`wtfCTF{H4RE_15_F45T3R}`<br>
On CyberChef (for example):
endianness -> little <br>
input token -> 949d407e5e298705f96a81816a084778c000adc2e933<br>
key -> a51b91726358c3801469ac4750583789<br>
IV -> a42ccf7adecc21a8<br>