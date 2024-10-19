# Solution to the Q3 (List of commands)

```
ls
doll.jpg  mat_doll.jpg
```
```
binwalk doll.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
32707         0x7FC3          Zip archive data, at least v2.0 to extract, compressed size: 98318, uncompressed size: 98399, name: doll2.jpg
131171        0x20063         End of Zip archive, footer length: 22

```
```
binwalk -e doll.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
32707         0x7FC3          Zip archive data, at least v2.0 to extract, compressed size: 98318, uncompressed size: 98399, name: doll2.jpg
131171        0x20063         End of Zip archive, footer length: 22

```
```
cd _doll.jpg.extracted/
```
```
ls
7FC3.zip  doll2.jpg
```
```
binwalk -e doll2.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
32707         0x7FC3          Zip archive data, at least v2.0 to extract, compressed size: 65524, uncompressed size: 65586, name: doll3.jpg
98276         0x17FE4         End of Zip archive, footer length: 22
98377         0x18049         End of Zip archive, footer length: 22

```
```
cd _doll2.jpg.extracted/
```
```
binwalk -e doll3.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
32707         0x7FC3          Zip archive data, at least v2.0 to extract, compressed size: 32665, uncompressed size: 32728, name: .220px-Russian_Doll (copy 3).JPG
65564         0x1001C         End of Zip archive, footer length: 22


```
```
cd _doll3.jpg.extracted/

```
```
ls
7FC3.zip
```
```
ls -a
 .   ..  '.220px-Russian_Doll (copy 3).JPG'   7FC3.zip
```
```
exiftool '.220px-Russian_Doll (copy 3).JPG'
ExifTool Version Number         : 12.76
File Name                       : .220px-Russian_Doll (copy 3).JPG
Directory                       : .
File Size                       : 33 kB
File Modification Date/Time     : 2024:10:04 00:20:00+05:30
File Access Date/Time           : 2024:10:04 00:26:01+05:30
File Inode Change Date/Time     : 2024:10:05 01:16:51+05:30
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Comment                         : wtfCTF{ThEr3_r_5}
Image Width                     : 220
Image Height                    : 465
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 220x465
Megapixels                      : 0.102
```
