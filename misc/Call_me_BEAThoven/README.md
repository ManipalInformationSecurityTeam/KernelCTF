# Call me BEAThoven
Hey, can someone help me find my Music?? It was on an A3 sheet.....


hints: 
1. not all frequencies are from real music
2. all alphabets are incrementing by 50


Solution:

In this challenge, you'll encounter an audio file filled with a series of tones representing a secret message. The tones have been generated based on unique frequencies for different letters, inspired by the Swedish Military Phonetic Alphabet. Your goal is to reverse-engineer the audio pattern and decipher the hidden message.

Description:
1. The audio file contains a sequence of sine wave tones.
2. Each letter of the alphabet corresponds to a unique frequency.
3. Spaces between words are represented by silence.
4. No additional information about the frequencies used is provided.
5. The flag is hidden within the decoded message.

Steps:
1. analyze frquencies using audacity
2. Extract and map frequencies to each letter.
3. Decode the message flag is wrapped in wtfCTF{}.

FLAG : wtfCTF{Tones_Can_Unlock_Secrets}

