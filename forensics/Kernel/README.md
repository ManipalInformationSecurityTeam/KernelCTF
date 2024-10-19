# K3rnE1:

## 13/10/24:

## The image: 
---
![popcorn.png](./popcorn.png)

---

## Approach:

this image contains the flag `wtfCTF{P0pcrn}` in its metadata in the comment.<br>

use exiftool to find it:
```
exiftool popcorn.png
ExifTool Version Number         : 12.76
.
.
.
.
Comment                         : wtfCTF{P0pcrn}
Image Size                      : 806x511
Megapixels                      : 0.412
```
