## Question

Let's go on a little road trip!

*[0.png]*

flag is wrapped in wtfCTF{}
## Hints

1) No Image Manipulation is required for this question

2) There might be some metadata in the QRs themselves

3) https://www.qrcode.com/en/about/version.html (if given reduce points)

## Solution
Each QR code has a broken link to another QR code- The link is either put in a URL shortener or repeated multiple times, either way you can get the link from the repeated strings

The fact that the links are repeated is padding to change the amount of data in a QR code, which is where you can realize that the size of the QR codes is different

QR codes have versions from 1-40, these QR codes are specifically using the binary encoding, all data taken from the website: https://www.qrcode.com/en/about/version.html

So for example, QR 5 has the text "https://drive.proton.me/urls/HV6XY8A26C#8ILLgMnXo52Hhttps://" which is 60 bytes long, at Q Error Correction Level, making it version 5

This is one of the few QRs which are not in H Error Correction Level, in general, all QRs fit the exact number of bytes required to be that version. The versions of the QR can also be read from the physical pixel size of the QRs, after that, each version correlates to a letter(A is 1, B is 2 and so on)

Here is every image with the QR Version and it's corresponding letter

0.png	Version 1	A
1.png	Version 2 	B
2.png	Version 5	E
3.png	Version 1 	A
4.png	Version 21	U
5.png	Version 20 	T
6.png	Version 9 	I
7.png	Version 6 	F
8.png	Version 21	U
9.png	Version 12 	L
10.png	Version 22 	V
11.png	Version 22	V
12.png	Version 9	I
13.png	Version 19 	S
14.png	Version 20	T
15.png	Version 1 	A

At the end, the flag is wrapped in wtfCTF{}, making it wtfCTF{ABEAUTIFULVVISTA}
