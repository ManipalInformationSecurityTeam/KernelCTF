# Challenge 2: TH3 C4V3 0F C4V3 J0HN50N

## Challenge Description
I am blind to the answer to this one. Quite perplexed. Stuck between worlds.

## Files Provided
- im.png

## Solution

### Key Information
- Flag Format: wtfCTF{FLAG}
- Key String: EASYPEEZYLEMONSQUEEZY

### Procedure
1. Image Analysis:
   - The provided image (im.png) has dimensions of 3468 × 2715 pixels.
   - These dimensions are significant as they represent the rearranged order of columns from the original image.

2. Image Reconstruction:
   - The columns of the image have been rearranged in the order: 3rd, 4th, 6th, 8th, and so on.
   - To obtain the original image, these columns need to be rearranged back to their correct positions.

3. Braille Decoding:
   - The reconstructed image contains Braille representations of words.
   - These Braille patterns correspond to the following words:
     Ebay, Amazon, Spotify, Youtube, Pizzahut, Eggzone, Evilcorp, Zara, Yorkshiretea, Lemontree, Earlgrey, Microsoft, Oyo, Netflix, Superdry, Quora, Underarmor, Enron, Easports, Zudio, Yahoo

4. Flag Construction:
   - Take the first letter of each decoded word.
   - Combine these letters to form the flag.
   - Enclose the resulting string in wtfCTF{}.

### Final Flag
wtfCTF{EASYPEEZYLEMONSQUEEZY}

## Hints
1. Enclose the flag in wtfCTF{}
2. Look into the depths of the data that is very meta (fr fr)
3. The columns of Rome may have fallen, but the order still remains in some alternate dimension. (NOT IN THE START.)

These hints point towards examining metadata, considering alternative dimensions or arrangements of the image, and focusing on the column order of the provided image.
