# Writeup For Question 1 (includes approach):
## 1-10-24
## Question Statement:
```
1010011001 10000011
where does the light of a candle not reach?
```
This consists of two binary encoded numbers, corresponding to '665' and '131'.
The next line is indicative of the fact that the answer to this question is in the txt file.

## Approach:

Converting the binary to decimal you get '665' and '131', initialy these seem like random numbers.
If the hint is understood properly, the contestant will run binwalk on the txt file:
```
binwalk candleQ.txt
```
In this they will get to know of a zip file.
Extracting it using
```
binwalk -e candleQ.txt
```
extracts the contents into a folder.

Opening the folder, we can see a scrambled image titled candle.ppm
opening this image in vim (after navigating into the extracted folder)
```
vim candle.ppm
```
we can notice that the pixel count is '345' and '91'
This needs to be replced by the '665' and '131' we have decoded from binary
changing the pixel count to the decoded one by editing the file in vim gives us an updated image.
Opening this image gives a sensible output image, which is ``wtfCTF{Und3r_1t}``
