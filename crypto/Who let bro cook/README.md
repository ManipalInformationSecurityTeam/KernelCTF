Q. WH0_L3T_BR0_C00K (100)

Question.

- First, we prepare the sauce.
- To make that, we need a TOMATO VINEGAR mix.
- We grate 6 cubes of cheese in the CHEEZER.

- For toppings, we need:
  - 32 Basil Leaves.
  - We put 13 inclusive preservatives on it, so that it doesn't ROT.

- The pizza thus prepared is:

BO8IFK5LVEHSVK5UTRLKRK55TAXQBD5XTNLQVA5ATZLRVEMHXEPSRZP0CH======

It's very tasty. Hope you enjoy it.

Documentation:

- They key is `wtfCTF{THISWASFUNTOCOOKHAHAHAHA}`

In order, it's passed through the ciphers:
- Vignere with key `TOMATO`. (Vinegar is essentially a pun on the word vinegar.)
- Caesar cipher with 6 shifts. (CHEEZER = Caesar, phonetically)
- Base32 cipher. `A-Z2-7=` (32 Basil = Base32)
- ROT13 cipher. `13`

Thus, the output would be the string given in the question.

To solve it, you must traverse in the reverse order.

- First, decode it using the ROT13 cipher.
- Then pass it through a Base32 decode.
- Then, decode it with a 6-shift Caesar cipher. `o=(c−6)mod26` would be the shift for any character `c`.
- Finally, decode it with a Vignere decoder with key `TOMATO`.

Thus, you achieve the flag.
