# C0lr_3ory:-
## 5-10-24
Question
---

Sometimes messages get lost in the noise. But there is still a trace left. FInd the message.

---
Approach
---

So, this question is presented in the form of an Image and an cisco packet tracer diagram? thats the hint.<br>
![this file](./twst.pkt)<br>
the image is divided into 3 differnt sections as is visible in ``new_q4.png`` .<br>
The image seems blank at first untill you realise that the hints point toward three RGB values.
These values are:
```
170,183,198

098,201,235

129,158,076
```
these values are important when they realise that the RGB values are the values of the color of the text that is hidden in the image.<br>
Now the trick to this question is that the text is highlighted in such a way that the highlight color is just one off the text color, making the change invisible to the naked eye.<br>
But if they find a software or online tool to extract the text based on the RGB values like this [site](https://onlinepngtools.com/extract-color-from-png)<br>
Like I did in the process.png image.<br>
They have to get the codes and find the individual parts of the flag and string them together to form ``wtfCTF{Sp3ctrum5_0f_rea1ity}``<br>
