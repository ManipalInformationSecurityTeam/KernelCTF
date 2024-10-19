This is the code that generates japanese:
#+begin_src python
  brainfuck = "+[--->++<]>++++.[--->++++<]>++.[->+++<]>-.------------.+[-->+<]>++.+++.-[->++<]>.++[->+++<]>.---.++++++."
emoji_code =  0x3040
print(ord('+'))
for c in brainfuck:
    print(chr(ord(c)+emoji_code),end="")
#+end_src

In the quiet village of Mizumura, there lived an old samurai named Ryuunosuke. Once a famed warrior, he had now taken up the role of teacher, imparting wisdom and discipline to the village’s children. His dojo, nestled between the mountains and a misty river, had 3,040 students. It was said that no one else could command such respect, teaching each child the way of the sword, honor, and self-discipline.

The children came daily, their laughter and chatter filling the air as they practiced under his
watchful eye. But then, something strange began to happen. A child would be absent one day, and
their parents would claim they had never existed. Ryuunosuke noticed it too—the roll he kept of his
students’ names slowly began to shrink. First, it was a few. Then dozens. Then hundreds. And yet, no
one seemed to remember those who vanished, as if they had been plucked from existence. One day, he
finds a note filled with rubbish. Could you help him crack the code?
#+quote
に゛ねねねまににぼゝまににににの゛ねねねまににににぼゝまににの゛ねまにににぼゝまねのねねねねねねねねねねねねのに゛ねねまにぼゝまににのにににのね゛ねまににぼゝまのにに゛ねまにににぼゝまのねねねのににににににの
#+end_quote

Need a riddle to hide 3040
